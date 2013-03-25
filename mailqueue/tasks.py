import celery
from .models import MailerMessage

@celery.task(name="tasks.send_mail")
def send_mail(pk):
    message = MailerMessage.objects.get(pk=pk)
    message.send()
