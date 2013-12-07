from django.conf import settings


def get_storage():
	if getattr(settings, 'MAIL_QUEUE_STORAGE', False):
		from django.core.files.storage import FileSystemStorage
		fs = FileSystemStorage(location=settings.MEDIA_ROOT)
	else:
		fs = None
	return fs
