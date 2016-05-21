[![Build Status](https://travis-ci.org/dstegelman/django-mail-queue.png?branch=master)](https://travis-ci.org/dstegelman/django-mail-queue)

Django Mail Queue
=================

Mail Queue provides an easy and simple way to send email.  Each email is saved and queued up either in
real time or with Celery.  As always, feedback, bugs, and suggestions are welcome.

Documentation
-------------

http://readthedocs.org/docs/django-mail-queue/en/latest/

Mail Queue provides an admin interface to view all attempted emails and actions for resending failed messages.

![image](http://cl.ly/image/1j2S3f021z0M/Screen%20Shot%202012-11-18%20at%205.45.17%20PM.png)


Support/Help/Spam/Hate Mail
---------------------------

If you have questions/problems/suggestions the quickest way to reach me to is simply add a GitHub issue to this project.

Running the Tests Locally
-------------------------

```
pip install django
pip install -r requirements.txt

py.test mailqueue
```
