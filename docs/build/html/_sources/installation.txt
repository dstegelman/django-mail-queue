Quick Start Guide
=================


Requirements
------------

Interactive API Docs requires::

    south
    django 1.3 or greater



Installation
------------

Using ``pip``::

    pip install https://github.com/dstegelman/django-interactive-api-docs

Go to https://github.com/dstegelman/django-interactive-api-docs if you need to download a package or clone the repo.


Setup
-----

Open ``settings.py`` and add ``api_docs`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'api_docs',
        'south',
    )
    
Open ``settings.py`` and add ``'api_docs.middleware.ContentTypeMiddleware'`` to middleware::

    MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'api_docs.middleware.ContentTypeMiddleware',
)

Add URL-patterns::

    urlpatterns = patterns('',
        (r'^docs/', include('api_docs.urls')),
    )
    
Static Files
------------

If you intend on using the default template, you'll need to grab the static files off of https://github.com/dstegelman/django-interactive-api-docs and copy them into an api_docs folder that can be seen 
by your static web server.

