from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clear$', views.clear_sent_messages, name='clear_sent_messages'),
    url(r'^$', views.run_mail_job, name='run_mail_job'),
]
