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

Go to https://github.com/kstateome/django-mail-queue if you need to download a package or clone the repo.

Setup
-----

Open ``settings.py`` and add ``api_docs`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'mailqueue',
        'south',
    )
    

Add URL-patterns::

    urlpatterns = patterns('',
        (r'^mail-queue/', include('mailqueue.urls')),
    )

Cron Job (optional)
-------------------

Setup a cron job to hit the root of mail-queue.  So the example above would hit /mail-queue.  This runs the mail queue which grabs emails and sends them.  To decrease load, it only tries
to send 30 emails at a time.


Celery (Optional)
------

Celery is disabled by default, you can turn it on the use of Celery and send emails in real time using ``MAILQUEUE_CELERY`` in settings::

    MAILQUEUE_CELERY = True

Instead of using the cron job the celery task worker will attempt to send email email when it's saved.  The cron job will clean up any emails that get lost.
