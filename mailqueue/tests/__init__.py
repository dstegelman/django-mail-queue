import shutil
import os.path
from django.core import mail
from django.core.files import File
from django.test import TestCase
from django.conf import settings
from .utils import create_email

class MailQueueTestCase(TestCase):
    def setUp(self):
        self.TEST_ROOT = os.path.abspath(os.path.dirname(__file__))

        # at the moment there are no tests for our celery tasks
        self.MAILQUEUE_CELERY = getattr(settings, "MAILQUEUE_CELERY", False)
        setattr(settings, "MAILQUEUE_CELERY", False)

    def _setUp_files(self):
        self.small_file = File(open(os.path.join(self.TEST_ROOT, "attachments", "small.txt"), "r"))
        self.large_file = File(open(os.path.join(self.TEST_ROOT, "attachments", "big.pdf"), "rb"))

    def tearDown(self):
        setattr(settings, "MAILQUEUE_CELERY", self.MAILQUEUE_CELERY)

        try:
            shutil.rmtree(os.path.join(self.TEST_ROOT, "../../mail-queue"))
        except OSError:
            pass

    def test_email(self):
        create_email(subject="Test email")
        self.assertEqual(mail.outbox[0].subject, "Test email")

    def test_single_bcc(self):
        create_email(bcc_address="bcc@mail.co.uk")
        self.assertEqual(mail.outbox[0].bcc, ["bcc@mail.co.uk"])

    def test_multiple_bcc(self):
        create_email(bcc_address="bcc_one@mail.co.uk, bcc_two@mail.co.uk")
        self.assertEqual(mail.outbox[0].bcc, ["bcc_one@mail.co.uk", "bcc_two@mail.co.uk"])

    def test_add_attachment(self):
        self._setUp_files()

        test_message = create_email(do_not_save=True)
        test_message.add_attachment(self.small_file)
        test_message.save()

        self.assertEqual(mail.outbox[0].attachments[0][0], "small.txt")
        self.assertEqual(mail.outbox[0].attachments[0][1], b"This is a small attachment.\n")

    def test_add_large_attachment(self):
        self._setUp_files()

        test_message = create_email(do_not_save=True)
        test_message.add_attachment(self.small_file)
        test_message.save()

        self.assertEqual(len(mail.outbox[0].attachments), 1)

    def test_add_multiple_attachments(self):
        self._setUp_files()

        test_message = create_email(do_not_save=True)
        test_message.add_attachment(self.small_file)
        test_message.add_attachment(self.large_file)
        test_message.save()

        self.assertEqual(len(mail.outbox[0].attachments), 2)

    def test_mailqueue_up(self):
        setattr(settings, "MAILQUEUE_QUEUE_UP", True)
        create_email(subject='Test Email')
        self.assertEqual(mail.outbox, [])
        setattr(settings, "MAILQUEUE_QUEUE_UP", False)
