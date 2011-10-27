from django.conf.urls.defaults import patterns, include, url
from mailqueue.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', run_mail_job, name='home'),

)