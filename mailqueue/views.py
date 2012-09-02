from mailqueue.models import MailerMessage
from django.http import HttpResponse

def run_mail_job(request):
    emails = MailerMessage.objects.filter(sent=False)[:30]
    for email in emails:
        email.send()
    response = HttpResponse()
    response.status_code = 200
    return response