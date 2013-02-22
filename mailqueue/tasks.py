from celery.task import task


#Cached Services
@task()
def send_mail(mailer):
    mailer.send()


@task()
def clear_sent_messages():
    from mailqueue.models import MailerMessage
    MailerMessage.objects.clear_sent_messages()