from django.shortcuts import render

from mailqueue.models import MailerMessage
# Create your views here.

def create_mail_message(request):
    new_message = MailerMessage()
    new_message.subject = "My Subject"
    new_message.to_address = "someone@example.com"
    new_message.cc_address = "carboncopy@yo.com"
    new_message.bcc_address = "myblindcarboncopy@yo.com"
    new_message.from_address = "hello@example.com"
    new_message.content = "Mail content"
    new_message.html_content = "<h1>Mail Content</h1>"
    new_message.app = "Name of your App that is sending the email."
    new_message.save()

    return render(request, 'index.html')
