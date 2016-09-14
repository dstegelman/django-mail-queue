from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
from .models import MailerStorage


def get_storage():
    fs = None
    if getattr(settings, 'MAILQUEUE_STORAGE', False):
        fs = MailerStorage() if hasattr(settings, 'MAILQUEUE_ROOT') else FileSystemStorage(location=settings.MEDIA_ROOT)
    return fs


def upload_to(instance, filename):
    # Because instead of filesystem, email message can have multiple attachments with the same filename
    return 'mailqueue-attahcments/{0}_{1}'.format(get_random_string(length=24), filename)
