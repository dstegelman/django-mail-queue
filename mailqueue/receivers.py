from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from mailqueue.models import MailerMessage
from . import defaults


@receiver(post_save, sender=MailerMessage)
def send_post_save(sender, instance, signal, *args, **kwargs):
    if getattr(instance, "do_not_send", False):
        instance.do_not_send = False
        return

    if not getattr(settings, 'MAILQUEUE_QUEUE_UP', defaults.MAILQUEUE_QUEUE_UP):
        # If mail queue up is set, wait for the cron or management command
        # to send any email.
        instance.send_mail()
