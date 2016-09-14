from django.conf import settings
from django.core.files.storage import FileSystemStorage


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
