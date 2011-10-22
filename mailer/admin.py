from django.contrib import admin
from mailer.models import MailerMessage

class MailerAdmin(admin.ModelAdmin):
    list_display = ('app', 'subject', 'to_address', 'sent')


admin.site.register(MailerMessage, MailerAdmin)