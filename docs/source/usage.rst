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
and wait for the next time the job is called.  Mail Queue sends html emails by default.  I may add functionality to send text emails,
but it is not present yet.  Of course, the BCC address is optional, as well as html content.



