import factory

from mailqueue.models import MailerMessage


class MailFactory(factory.DjangoModelFactory):
    subject = "Test email"
    to_address = "foo@mail.co.uk"
    from_address = "noreply@mail.co.uk"
    content = "We are the Knights who say... NI"
    app = "Test suite"

    class Meta:
        model = MailerMessage
