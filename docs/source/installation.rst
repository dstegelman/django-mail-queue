Quick Start Guide
=================


Requirements
------------

Django Mail Queue requires::

    south
    django 1.4 or greater

Installation
------------

Using ``pip``::

    pip install django-mail-queue

Go to https://github.com/dstegelman/django-mail-queue if you need to download a package or clone the repo.

Setup
-----

Open ``settings.py`` and add ``api_docs`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'mailqueue',
        'south',
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
