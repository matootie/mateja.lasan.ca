import os
from website.settings.common import *


SECRET_KEY = 'not-a-real-key'
DEBUG = True
WSGI_APPLICATION = 'website.wsgi.development.application'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'serve/static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'serve/media/')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), }, }

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1', ]
