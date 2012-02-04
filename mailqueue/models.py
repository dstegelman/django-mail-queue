#---------------------------------------------#
#
#
# Mailer will queue up emails, Try to send them
# and keep track of if they are sent or not.
# Should be executed with a cron job.
#
#
#
#
#
#---------------------------------------------#
from django.db import models
from django.core.mail import EmailMultiAlternatives
from mailqueue.tasks import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class MailerMessage(models.Model):
    subject = models.CharField(max_length=250, blank=True, null=True)
    to_address = models.EmailField(max_length=250)
    from_address = models.EmailField(max_length=250)
    content = models.TextField(blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)
    app = models.CharField(max_length=250, blank=True, null=True)
    sent = models.BooleanField(default=False, editable=False)
    
    def __unicode__(self):
        return self.subject
                
    def send(self):
        if not self.sent:
            try:
                subject, from_email, to = self.subject, self.from_address, self.to_address
                text_content = self.content
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to]) 
                if self.html_content:
                    html_content = self.html_content
                    msg.attach_alternative(html_content, "text/html")
                msg.send()
                self.sent = True
                self.save()
            except:
                pass


@receiver(post_save, sender=MailerMessage)
def send_post_save(sender, instance, signal, *args, **kwargs):
    send_mail.delay(instance)