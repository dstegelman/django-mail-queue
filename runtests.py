__author__ = 'derek'
import os, sys
from django.conf import settings

DIRNAME = os.path.dirname(__file__)
settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                           }
                   },
                   ROOT_URLCONF='mailqueue.urls',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'mailqueue',),
                   USE_TZ=True)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['mailqueue', ])
if failures:
    sys.exit(failures)