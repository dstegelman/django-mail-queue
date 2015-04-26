Quick Start Guide
=================

As of 2.0 Django Mail Queue is now Python 3 compatable!


Requirements
------------

Django Mail Queue requires::

    python 2.7 or greater
    south #If using Django < 1.7
    django 1.5 or greater

Django Mail Queue is tested against Python 2.7, 3.3 and Django 1.5, 1.6, 1.7 and 1.8.

Installation
------------

Using ``pip``::

    pip install django-mail-queue

Go to https://github.com/dstegelman/django-mail-queue if you need to download a package or clone the repo.

Setup
-----

Open ``settings.py`` and add ``mailqueue`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'mailqueue',
        'south', # only needed for < 1.7
    )



Cron Job (optional)
-------------------

A cron job can be set up to work one of two ways: using a management command or an HTTP request. Both methods run the mail queue which grabs emails and sends them. To decrease load, it only tries to send 30 emails at a time. This number can be changed by using ``MAILQUEUE_LIMIT`` in settings::

    MAILQUEUE_LIMIT = 50

Using the management command::

    python manage.py send_queued_messages

You can also override ``MAILQUEUE_LIMIT`` by using the ``--limit`` or ``-l`` option::

    python manage.py send_queued_messages --limit=10

HTTP request::

    urlpatterns = patterns('',
        (r'^mail-queue/', include('mailqueue.urls')),
    )

If you're running cron from another machine or can't run python directly, you can add the above to urls.py and use a utility like curl to hit /mail-queue/.


Celery (Optional)
------

Celery is disabled by default, you can turn it on the use of Celery and send emails in real time using ``MAILQUEUE_CELERY`` in settings::

    MAILQUEUE_CELERY = True

Instead of using the cron job the celery task worker will attempt to send email email when it's saved.  The cron job will clean up any emails that get lost.

Queue Mail (Optional)
----------

You can truly queue up mail and send only with the cron job or management command by adding ``MAILQUEUE_QUEUE_UP = True`` to your settings file.  By
default this functionality is turned off.

Misc Settings
-------------

You can force mail queue to use default file system storage with MEDIA_ROOT as the storage folder.  You may want to do this
because by default mail queue will use your default file storage, and attachments are known to not work against various
storages such as S3 Boto.

To force Django's File System storage::

    MAILQUEUE_STORAGE = True
