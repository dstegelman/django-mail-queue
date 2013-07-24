from django.contrib import admin
from django.conf import settings

from mailqueue.models import MailerMessage, Attachment
from mailqueue import defaults


class AttachmentInline(admin.TabularInline):
    model = Attachment


class MailerAdmin(admin.ModelAdmin):
    list_display = ('app', 'subject', 'to_address', 'sent', 'last_attempt')
    search_fields = ['to_address', 'subject', 'app', 'bcc_address']
    actions = ['send_failed']
    inlines = [AttachmentInline]

    def send_failed(self, request, queryset):
        emails = queryset.filter(sent=False)
        for email in emails:
            if getattr(settings, 'MAILQUEUE_CELERY', defaults.MAILQUEUE_CELERY):
                from mailqueue.tasks import send_mail
                send_mail.delay(email)
            else:
                email.send()
        self.message_user(request, "Emails queued.")

admin.site.register(MailerMessage, MailerAdmin)