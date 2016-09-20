from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string


class MailerStorage(FileSystemStorage):
    def __init__(self, location=None):
        if not location:
            location = settings.MAILQUEUE_ROOT
        FileSystemStorage.__init__(self, location=location)

    def url(self):
        return ''


def get_storage():
    fs = None
    if getattr(settings, 'MAILQUEUE_STORAGE', False):
        fs = MailerStorage() if hasattr(settings, 'MAILQUEUE_ROOT') \
            else FileSystemStorage(location=settings.MEDIA_ROOT)
    return fs


def upload_to(instance, filename):
    # Because filename may also contain path
    # which is unneeded and may be harmful
    filename = filename.split('/')[-1]
    # Because instead of filesystem, email message
    # can have multiple attachments with the same filename
    return 'mailqueue-attahcments/{0}_{1}'.format(get_random_string(length=24), filename)
