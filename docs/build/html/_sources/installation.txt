Quick Start Guide
=================


Requirements
------------

Django Mail Queue requires::

    south
    django 1.3 or greater



Installation
------------

Using ``pip``::

    pip install git+git://github.com/dstegelman/django-mail-queue.git

Go to https://github.com/dstegelman/django-mail-queue if you need to download a package or clone the repo.


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
    
Cron Job
--------

Setup a cron job to hit the root of mail-queue.  So the example above would hit /mail-queue.  This runs the mail queue which grabs emails and sends them.  To decrease load, it only tries
to send 30 emails at a time.

