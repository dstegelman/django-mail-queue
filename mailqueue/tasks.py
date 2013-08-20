from celery.task import task
from .models import MailerMessage

@task(name="tasks.send_mail")
def send_mail(pk):
    message = MailerMessage.objects.get(pk=pk)
    message._send()

@task()
def clear_sent_messages():
    from mailqueue.models import MailerMessage
    MailerMessage.objects.clear_sent_messages()
