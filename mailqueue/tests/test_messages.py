import shutil
import os.path

from django.core import mail
from django.core.files import File
from django.test import TestCase
from django.conf import settings

from ..models import MailerMessage
from .utils import create_email
from .factories import MailFactory


class MailQueueTestCase(TestCase):
    def setUp(self):
        self.TEST_ROOT = os.path.abspath(os.path.dirname(__file__))

        # at the moment there are no tests for our celery tasks
        self.MAILQUEUE_CELERY = getattr(settings, "MAILQUEUE_CELERY", False)
        setattr(settings, "MAILQUEUE_CELERY", False)

    def _setUp_files(self):
        self.large_file = File(open(os.path.join(self.TEST_ROOT, "attachments", "big.pdf"), "rb"))

    def tearDown(self):
        setattr(settings, "MAILQUEUE_CELERY", self.MAILQUEUE_CELERY)

        try:
            shutil.rmtree(os.path.join(self.TEST_ROOT, "../../mail-queue"))
        except OSError:
            pass

    def test_clear_messages(self):
        MailFactory.create(subject='old_mail')
        MailFactory.create(subject='new_mail')

        self.assertEqual(MailerMessage.objects.count(), 2)

        MailerMessage.objects.clear_sent_messages(offset=24)
        self.assertEqual(MailerMessage.objects.count(), 2)

        MailerMessage.objects.clear_sent_messages()
        self.assertEqual(MailerMessage.objects.count(), 0)

    def test_email(self):
        MailFactory.create(subject='Test email')
        self.assertEqual(mail.outbox[0].subject, "Test email")

    def test_ugly_addresses(self):
        addresses = '''
        Jane@mail.co.uk,
        john@mail.co.uk, ,  julie@mail.co.uk,
        '''
        cc_addresses = '''
                  , Lou@mail.co.uk,
                lisa@mail.co.uk, ,  lori@mail.co.uk,
                ,
                '''
        bcc_addresses = '''
          , Lou@mail.co.uk,
        lisa@mail.co.uk, ,  lori@mail.co.uk,
        ,
        '''
        MailFactory.create(to_address=addresses, cc_address=cc_addresses, bcc_address=bcc_addresses)

        self.assertEqual(mail.outbox[0].to, ["Jane@mail.co.uk", "john@mail.co.uk",
                                             "julie@mail.co.uk"])
        self.assertEqual(mail.outbox[0].cc, ["Lou@mail.co.uk", "lisa@mail.co.uk",
                                             "lori@mail.co.uk"])
        self.assertEqual(mail.outbox[0].bcc, ["Lou@mail.co.uk", "lisa@mail.co.uk",
                                              "lori@mail.co.uk"])

    def test_multiple_to(self):
        addresses = 'Jane@mail.co.uk,john@mail.co.uk,julie@mail.co.uk'
        MailFactory.create(to_address=addresses)
        self.assertEqual(mail.outbox[0].to, ["Jane@mail.co.uk", "john@mail.co.uk",
                                             "julie@mail.co.uk"])

    def test_single_cc(self):
        MailFactory.create(cc_address="cc@mail.co.uk")
        self.assertEqual(mail.outbox[0].cc, ["cc@mail.co.uk"])

    def test_multiple_cc(self):
        MailFactory.create(cc_address="cc_one@mail.co.uk, cc_two@mail.co.uk")
        self.assertEqual(mail.outbox[0].cc, ["cc_one@mail.co.uk", "cc_two@mail.co.uk"])

    def test_single_bcc(self):
        MailFactory.create(bcc_address="bcc@mail.co.uk")
        self.assertEqual(mail.outbox[0].bcc, ["bcc@mail.co.uk"])

    def test_multiple_bcc(self):
        MailFactory.create(bcc_address="bcc_one@mail.co.uk, bcc_two@mail.co.uk")
        self.assertEqual(mail.outbox[0].bcc, ["bcc_one@mail.co.uk", "bcc_two@mail.co.uk"])

    def test_send_mail_reply_to(self):
        """Testing creating a MailerMessage and send mail"""
        reply_to = "reply_to@mail.co.uk"
        mail = MailFactory.create(reply_to=reply_to)

        self.assertEqual(mail.sent, True)
        self.assertEqual(mail.reply_to, reply_to)

    def test_add_attachment(self):
        self._setUp_files()

        test_message = create_email(do_not_save=True)
        test_message.add_attachment(self.large_file)
        test_message.save()

        self.assertEqual(mail.outbox[0].attachments[0][0], "big.pdf")

    def test_add_large_attachment(self):
        self._setUp_files()

        test_message = create_email(do_not_save=True)
        test_message.add_attachment(self.large_file)
        test_message.save()

        self.assertEqual(len(mail.outbox[0].attachments), 1)

    def test_add_multiple_attachments(self):
        self._setUp_files()

        test_message = create_email(do_not_save=True)
        test_message.add_attachment(self.large_file)
        test_message.add_attachment(self.large_file)
        test_message.save()

        self.assertEqual(len(mail.outbox[0].attachments), 2)

    def test_mailqueue_up(self):
        setattr(settings, "MAILQUEUE_QUEUE_UP", True)
        MailFactory.create(subject='Test Email')
        self.assertEqual(mail.outbox, [])
        setattr(settings, "MAILQUEUE_QUEUE_UP", False)
