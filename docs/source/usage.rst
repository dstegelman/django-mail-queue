Usage
=====


To Send an Email
----------------

Create a new MailerMesage() object::

    from mailqueue.models import MailerMessage

    new_message = MailerMessage()
    new_message.subject = "My Subject"
    new_message.to_address = "someone@example.com"
    new_message.bcc_address = "myblindcarboncopy@yo.com"
    new_message.from_address = "hello@example.com"
    new_message.content = "Mail content"
    new_message.html_content = "<h1>Mail Content</h1>"
    new_message.app = "Name of your App that is sending the email."
    new_message.save()

When save is called, Django will immediately try to send the email.  Should it fail, it will be marked as unsent,
and wait for the next time the job is called.  Of course, the BCC address is optional, as well as html content.



Attaching Files
------------------------

File attachments can be added to the e-mail with MailerMessage's `add_attachment` method::

    from mailqueue.models import MailerMessage
    from django.core.files import File

    message = MailerMessage(to_address="foo@mail.com", from_address="bar@mail.com")

    photo_one = File(open("Poznan_square.jpg", "r"))
    message.add_attachment(photo_one)

    # …you can add more than one file attachment
    photo_two = File(open("Poznan_Malta-lake.jpg", "r"))
    message.add_attachment(photo_two)

    message.save()



Sending to Multiple Recipients
------------------------------

To include more than one BCC in your email, just separate the addresses with a comma::

    message.bcc_address = "one@mail.com, two@mail.com, three@mail.com"

As of version 2.2.0 multiple recipients may be included in the `to_address` field as well::

    message.bcc_address = "one@mail.com, two@mail.com, three@mail.com"


Using the Management Command
----------------------------

You can use the management command to send email::

    python manage.py send_queued_messages --limit=20
