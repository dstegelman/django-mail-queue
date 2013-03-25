from celery.task import task

@task(name="tasks.send_mail")
def send_mail(mailer):
    mailer.send()
