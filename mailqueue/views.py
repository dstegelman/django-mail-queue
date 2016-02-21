from django.http import HttpResponse

from mailqueue.models import MailerMessage


def run_mail_job(request):
    MailerMessage.objects.send_queued()

    response = HttpResponse()
    response.status_code = 200
    return response


def clear_sent_messages(request):
    MailerMessage.objects.clear_sent_messages()

    response = HttpResponse()
    response.status_code = 200
    return response
