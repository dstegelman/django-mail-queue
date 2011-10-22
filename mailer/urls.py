from django.conf.urls.defaults import patterns, include, url
from mailer.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', run_mail_job, name='home'),

)