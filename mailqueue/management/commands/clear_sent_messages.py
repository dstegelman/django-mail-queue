from django.core.management.base import BaseCommand

from mailqueue.models import MailerMessage


class Command(BaseCommand):
    help = 'Can be run as a cronjob or directly to clean out sent messages.'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('offset', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument('--offset',
                            action='store_true',
                            dest='offset',
                            default=False,
                            help='Only clear messages that are more than this many hours old')

    def handle(self, *args, **options):
        MailerMessage.objects.clear_sent_messages(offset=options['offset'])
