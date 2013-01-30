# -*- coding: utf-8 -*-
import django
import os
import sys

SITE_ID = 1

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

PYTHON_VERSION = '%s.%s' % sys.version_info[:2]
DJANGO_VERSION = django.get_version()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'rosetta.db')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'ROSETTA_TEST'
    }
}


#CACHES = {'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}

TEST_DATABASE_CHARSET = "utf8"
TEST_DATABASE_COLLATION = "utf8_general_ci"

DATABASE_SUPPORTS_TRANSACTIONS = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'rosetta',
]
LANGUAGE_CODE = "en"

LANGUAGES = (
    ('en', 'English'),
    ('ja', u'日本語'),
    ('xx', u'XXXXX'),
)

SOUTH_TESTS_MIGRATE = False

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)
STATIC_URL = '/static/'
ROOT_URLCONF = 'testproject.urls'

DEBUG = True
TEMPLATE_DEBUG = True

STATIC_URL = '/static/'
#SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
#ROSETTA_STORAGE_CLASS = 'rosetta.storage.SessionRosettaStorage'
ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage'
SECRET_KEY = 'empty'
