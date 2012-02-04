from django.contrib import admin
from mailqueue.models import MailerMessage

class MailerAdmin(admin.ModelAdmin):
    list_display = ('app', 'subject', 'to_address', 'sent')
    
    actions = ['send_failed']


    def send_failed(self, request, queryset):
        emails = queryset.filter(sent=False)
        for email in emails:
            email.send()
        self.message_user(request, "Emails sent.")


admin.site.register(MailerMessage, MailerAdmin)