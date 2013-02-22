from optparse import make_option

from django.core.management.base import BaseCommand

from mailqueue.models import MailerMessage

class Command(BaseCommand):
    help = 'Can be run as a cronjob or directly to send queued messages.'

    option_list = BaseCommand.option_list + (
        make_option(
            '--limit',
            '-l',
            action='store',
            type='int',
            dest='limit',
            help='Limit the number of emails to process'
        ),
    )

    def handle(self, *args, **options):
        MailerMessage.objects.send_queued(limit = options['limit'])