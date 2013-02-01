import unittest
from django.core import mail
from mailqueue.models import MailerMessage

class MailQueueTestCase(unittest.TestCase):

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
