from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from mailqueue.models import MailerMessage
from mailqueue import defaults

class Command(BaseCommand):
    help = 'Sends queued emails'

    option_list = BaseCommand.option_list + (
        make_option(
            '--limit',
            '-l',
            action='store',
            type='int',
            dest='limit',
            default=getattr(settings, 'MAILQUEUE_LIMIT', defaults.MAILQUEUE_LIMIT),
            help='Limit the number of emails to process'
        ),
    )

    def handle(self, *args, **options):
        limit = options['limit']

        emails = MailerMessage.objects.filter(sent=False)[:limit]
        for email in emails:
            email.send()
