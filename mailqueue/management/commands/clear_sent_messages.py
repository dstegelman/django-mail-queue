from optparse import make_option

from django.core.management.base import BaseCommand

from mailqueue.models import MailerMessage

class Command(BaseCommand):
    help = 'Can be run as a cronjob or directly to clean out sent messages.'

    option_list = BaseCommand.option_list + (
        make_option(
            '--offset',
            action='store',
            type='int',
            dest='offset',
            help='Only clear messages that are more than this many hours old'
        ),
    )

    def handle(self, *args, **options):
        MailerMessage.objects.clear_sent_messages(offset = options['offset'])
