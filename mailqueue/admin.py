from django.contrib import admin
from mailqueue.models import MailerMessage

class MailerAdmin(admin.ModelAdmin):
    list_display = ('app', 'subject', 'to_address', 'sent')


admin.site.register(MailerMessage, MailerAdmin)