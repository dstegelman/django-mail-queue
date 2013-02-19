from django.http import HttpResponse
from django.conf import settings

from mailqueue.models import MailerMessage
from mailqueue import defaults

def run_mail_job(request):
    limit = getattr(settings, 'MAILQUEUE_LIMIT', defaults.MAILQUEUE_LIMIT)
    emails = MailerMessage.objects.filter(sent=False)[:limit]
    for email in emails:
        email.send()
    response = HttpResponse()
    response.status_code = 200
    return response