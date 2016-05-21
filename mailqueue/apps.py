from django.apps import AppConfig


class MailQueueConfig(AppConfig):
    name = 'mailqueue'
    label = 'mailqueue'
    verbose_name = "Mail Queue"

    def ready(self):
        from mailqueue import receivers
