#---------------------------------------------#
#
#
# Mailer will queue up emails, Try to send them
# and keep track of if they are sent or not.
# Should be executed with a cron job.
#
#
#
#
#
#---------------------------------------------#
from django.db import models
from django.core.mail import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class MailerMessage(models.Model):
    subject = models.CharField(max_length=250, blank=True, null=True)
    to_address = models.EmailField(max_length=250)
    from_address = models.EmailField(max_length=250)
    content = models.TextField(blank=True, null=True)
    app = models.CharField(max_length=250, blank=True, null=True)
    sent = models.BooleanField(default=False, editable=False)
    
    def __unicode__(self):
        return self.subject
    
    
    def send(self):
        try:
            msg = EmailMessage(self.subject, self.content, self.from_address, [self.to_address])
            msg.content_subtype = "html"
            msg.send()
            self.sent = True
        except:
            self.sent = False
        self.save()
        
    
@receiver(post_save, sender=MailerMessage)
def send_reciever(sender, **kwargs):
    emails = MailerMessage.objects.filter(sent=False)[:30]
    for email in emails:
        email.send()
    
