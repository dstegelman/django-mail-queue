import pytest

from ..models import MailerMessage


@pytest.mark.django_db
def create_email(**kwargs):
    """
    Utility function to make creating MailerMessage instances easier when testing.

    You can create a MailerMessage with default options in the database::

        message = create_email()

    You can override default options::

        message = create_email(subject="My subject", content="My content")

    You can also avoid saving to the database::

        message = create_email(do_not_save=True)
    """
    defaults = {
        "subject": "Test email",
        "to_address": "foo@mail.co.uk",
        "from_address": "noreply@mail.co.uk",
        "content": "We are the Knights who say... NI.",
        "app": "Test suite"
    }

    defaults.update(**kwargs)

    if defaults.pop("do_not_save", False):
        return MailerMessage(**defaults)

    return MailerMessage.objects.create(**defaults)
