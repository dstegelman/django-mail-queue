from celery.task import task
from .models import MailerMessage

@task(name="tasks.send_mail", default_retry_delay=5, max_retries=5)
def send_mail(pk):
    message = MailerMessage.objects.get(pk=pk)
    message._send()
    
    # Retry when message is not sent
    if not message.sent:
        send_mail.retry([message.pk,])

@task()
def clear_sent_messages():
    from mailqueue.models import MailerMessage
    MailerMessage.objects.clear_sent_messages()
