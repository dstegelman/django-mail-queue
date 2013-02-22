from django.conf.urls import patterns, url

urlpatterns = patterns('mailqueue.views',
    url(r'^clear$', 'clear_sent_messages', name='clear_sent_messages'),
    url(r'^$', 'run_mail_job', name='run_mail_job'),
)