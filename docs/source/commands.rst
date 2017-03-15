Management Commands
===================

Send Queued messages
--------------------

You can use this management command to send email if you do not
setup a cron job or use celery.  You can specify a limit on the
amount of emails you want to attempt to send at one time.::

    python manage.py send_queued_messages 20


Clear Sent messages
-------------------

You can use a management command to clear out successfully sent emails
from the database::

    ./manage.py clear_sent_messages
