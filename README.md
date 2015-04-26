[![Build Status](https://travis-ci.org/dstegelman/django-mail-queue.png?branch=master)](https://travis-ci.org/dstegelman/django-mail-queue)
[![Pypi Version](https://pypip.in/v/django-mail-queue/badge.png)](https://crate.io/packages/django-mail-queue)


Django Mail Queue
=================

Mail Queue provides an easy and simple way to send email.  Each email is saved and queued up either in
real time or with Celery.  As always, feedback, bugs, and suggestions are welcome.

Python 3 Users!
---------------

Django 1.7 is only supported on Python 2 at this point.  There is an
outstanding bug in issue #47.  If you use Python 3 with Django 1.7 DO NOT UPGRADE
to 2.2.0.

Installation
------------

    pip install django-mail-queue

We officially support the 3 latest versions of Django as best as possible.  Currently this means
that we test and support Django 1.5 and greater on Python 2.7, 3.3, and 3.4

Read me some docs
-----------------

http://readthedocs.org/docs/django-mail-queue/en/latest/

Mail Queue provides an admin interface to view all attempted emails and actions for resending failed messages.

![image](http://cl.ly/image/1j2S3f021z0M/Screen%20Shot%202012-11-18%20at%205.45.17%20PM.png)


Support/Help/Spam/Hate Mail
---------------------------

If you have questions/problems/suggestions the quickest way to reach me to is simply add a GitHub issue to this project.
