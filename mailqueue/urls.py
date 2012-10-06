from django.conf.urls import patterns, url
from mailqueue.views import run_mail_job

urlpatterns = patterns('',
    url(r'^$', run_mail_job, name='run_mail_job'),
)