from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string


def get_storage():
    if getattr(settings, 'MAILQUEUE_STORAGE', False):
        try:
            location = settings.MAILQUEUE_ROOT
        except AttributeError:
            location = settings.MEDIA_ROOT
        fs = FileSystemStorage(location=location)
    else:
        fs = None
    return fs


def upload_to(instance, filename):
    # Because instead of filesystem, email message can have multiple attachments with the same filename
    return 'mailqueue-attahcments/{0}_{1}'.format(filename, get_random_string(length=24))
