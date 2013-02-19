from django.http import HttpResponse

from mailqueue.models import MailerMessage

def run_mail_job(request):
    MailerMessage.objects.send_queued()

    response = HttpResponse()
    response.status_code = 200
    return response