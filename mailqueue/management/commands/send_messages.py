from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from mailqueue.models import MailerMessage

class Command(BaseCommand):
    args = '[--limit=LIMIT]'
    help = 'Sends queued emails'

    option_list = BaseCommand.option_list + (
        make_option(
            '--limit',
            '-l',
            action='store',
            type='int',
            dest='limit',
            default=30,
            help='Limit the number of emails to process'),
        )

    def handle(self, *args, **options):
        limit = options['limit']
        print(limit)

        emails = MailerMessage.objects.filter(sent=False)[:limit]
        for email in emails:
            email.send()
