from django.test import TestCase
from mailqueue.models import MailerMessage
from .utils import create_email


class MailerMessageTestCase(TestCase):

    def test_send_mail_reply_to(self):
        """Testing creating a MailerMessage and send mail"""
        reply_to = "reply_to@mail.co.uk"
        mail = create_email(reply_to=reply_to)
        mail.send_mail()

        self.assertEqual(mail.sent, True)
        self.assertEqual(mail.reply_to, reply_to)
