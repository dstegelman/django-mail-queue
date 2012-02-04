from celery.task import task


#Cached Services
@task()
def send_mail(mailer):
    mailer.send()
