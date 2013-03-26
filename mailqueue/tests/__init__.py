import os.path
from django.core import mail
from mailqueue.models import MailerMessage
from django.core.files import File
from django.test import TestCase
from django.test.utils import override_settings

@override_settings(MAILQUEUE_CELERY=False)
class MailQueueTestCase(TestCase):

    def test_email(self):
        mail.outbox = []

        email = MailerMessage()
        email.subject = 'Test Email'
        email.to_address = 'foo@foo.com'
        email.from_address = 'nope@foo.com'
        email.content = 'Test'
        email.app = 'Test App'

        email.save()

        self.assertEqual(mail.outbox[0].subject, 'Test Email')

    def test_single_bcc(self):
        mail.outbox = []

        test_message = MailerMessage(subject = "Test E-mail",
                                     to_address = "foo@mail.co.uk",
                                     bcc_address = "test_1@mail.co.uk",
                                     from_address = "noreply@test.co.uk",
                                     content = "Test content",
                                     app = "Newsletter App")
        test_message.save()

        self.assertEqual(mail.outbox[0].bcc, ["test_1@mail.co.uk", ])

    def test_multiple_bcc(self):
        mail.outbox = []

        test_message = MailerMessage(subject = "Test E-mail",
                                     to_address = "foo@mail.co.uk",
                                     bcc_address = "test_1@mail.co.uk, test_2@mail.co.uk",
                                     from_address = "noreply@test.co.uk",
                                     content = "Test content",
                                     app = "Newsletter App")
        test_message.save()

        self.assertEqual(mail.outbox[0].bcc, ["test_1@mail.co.uk", "test_2@mail.co.uk", ])

    def test_add_attachment(self):
        TEST_ROOT = os.path.abspath(os.path.dirname(__file__))
        test_file = File(open(os.path.join(TEST_ROOT, "attachments", "small.txt"), "r"))

        mail.outbox = []

        test_message = MailerMessage(subject = "Test E-mail",
                                     to_address = "foo@mail.co.uk",
                                     from_address = "noreply@test.co.uk",
                                     content = "Test content",
                                     app = "Newsletter App")

        test_message.add_attachment(test_file)
        test_message.save()

        self.assertEqual( mail.outbox[0].attachments[0],
                          (u"small.txt", "This is a small attachment.\n", None) )

    def test_add_big_attachment(self):
        TEST_ROOT = os.path.abspath(os.path.dirname(__file__))
        test_file_big = File(open(os.path.join(TEST_ROOT, "attachments", "big.pdf"), "r"))

        mail.outbox = []

        test_message = MailerMessage(subject = "Test E-mail",
                                     to_address = "foo@mail.co.uk",
                                     from_address = "noreply@test.co.uk",
                                     content = "Test content",
                                     app = "Newsletter App")

        test_message.add_attachment(test_file_big)
        test_message.save()

        self.assertEqual(len(mail.outbox[0].attachments), 1)

    def test_add_multiple_attachments(self):
        TEST_ROOT = os.path.abspath(os.path.dirname(__file__))
        test_file_one = File(open(os.path.join(TEST_ROOT, "attachments", "small.txt"), "r"))
        test_file_two = File(open(os.path.join(TEST_ROOT, "attachments", "big.pdf"), "r"))

        mail.outbox = []

        test_message = MailerMessage(subject = "Test E-mail",
                                     to_address = "foo@mail.co.uk",
                                     from_address = "noreply@test.co.uk",
                                     content = "Test content",
                                     app = "Newsletter App")

        test_message.add_attachment(test_file_one)
        test_message.add_attachment(test_file_two)
        test_message.save()

        self.assertEqual(len(mail.outbox[0].attachments), 2)
