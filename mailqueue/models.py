#---------------------------------------------#
#
# Mailer will queue up emails, Try to send them
# and keep track of if they are sent or not.
# Should be executed with a cron job.
#
#---------------------------------------------#
import datetime
import logging
import os

logger = logging.getLogger(__name__)

from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from . import defaults


class MailerMessageManager(models.Manager):
    def send_queued(self, limit=None):
        if limit is None:
            limit = getattr(settings, 'MAILQUEUE_LIMIT', defaults.MAILQUEUE_LIMIT)

        for email in self.filter(sent=False)[:limit]:
            email.send()


class MailerMessage(models.Model):
    subject = models.CharField(max_length=250, blank=True, null=True)
    to_address = models.EmailField(max_length=250)
    bcc_address = models.EmailField(max_length=250, blank=True, null=True)
    from_address = models.EmailField(max_length=250)
    content = models.TextField(blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)
    app = models.CharField(max_length=250, blank=True, null=True)
    sent = models.BooleanField(default=False, editable=False)
    last_attempt = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, editable=False)

    objects = MailerMessageManager()

    def __unicode__(self):
        return self.subject

    def add_attachment(self, attachment):
        """
        Takes a Django `File` object and creates an attachment for this mailer message.
        """
        if self.pk is None:
            self._save_without_sending()

        Attachment.objects.create(email=self, file_attachment=attachment)

    def _save_without_sending(self, *args, **kwargs):
        """
        Saves the MailerMessage instance without sending the e-mail. This ensures
        other models (e.g. `Attachment`) have something to relate to in the database.
        """
        self.do_not_send = True
        super(MailerMessage, self).save(*args, **kwargs)

    def send(self):
        if not self.sent:
            if getattr(settings, 'USE_TZ', False):
                # This change breaks SQLite usage.
                from django.utils.timezone import utc
                self.last_attempt = datetime.datetime.utcnow().replace(tzinfo=utc)
            else:
                self.last_attempt = datetime.datetime.now()

            subject, from_email, to = self.subject, self.from_address, self.to_address
            text_content = self.content
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            if self.html_content:
                html_content = self.html_content
                msg.attach_alternative(html_content, "text/html")
            if self.bcc_address:
                if ',' in self.bcc_address:
                    msg.bcc = [ email.strip() for email in self.bcc_address.split(',') ]
                else:
                    msg.bcc = [self.bcc_address, ]

            # Add any additional attachments
            for attachment in self.attachment_set.all():
                msg.attach_file(os.path.join(settings.MEDIA_ROOT, attachment.file_attachment.name))
            try:
                msg.send()
                self.sent = True
            except Exception, e:
                self.do_not_send = True
                logger.error('Mail Queue Exception: {0}'.format(e))

            self.save()


class Attachment(models.Model):
    file_attachment = models.FileField(upload_to='mail-queue/attachments', blank=True, null=True)
    email = models.ForeignKey(MailerMessage, blank=True, null=True)

    def __unicode__(self):
        return self.file_attachment.name

@receiver(post_save, sender=MailerMessage)
def send_post_save(sender, instance, signal, *args, **kwargs):
    if getattr(instance, "do_not_send", False):
        instance.do_not_send = False
        return

    if getattr(settings, 'MAILQUEUE_CELERY', defaults.MAILQUEUE_CELERY):
        from mailqueue.tasks import send_mail
        send_mail.delay(instance.pk)
    else:
        instance.send()
