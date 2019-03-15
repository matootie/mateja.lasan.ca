import os
import dj_database_url


from website.settings.common import *


SECRET_KEY = os.environ['DJANGO_KEY']
REDIS_URL = os.environ['REDIS_URL']

DEBUG = False
WSGI_APPLICATION = 'website.wsgi.production.application'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AWS_ACCESS_KEY_ID = os.environ['AWS_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET']
AWS_STORAGE_BUCKET_NAME = 'mateja-lasan-ca'
AWS_S3_CUSTOM_DOMAIN = '%s.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400', }
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = None
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'website.storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'website.storage_backends.MediaStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'), ]

DATABASES = {
    'default': dj_database_url.config(), }

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient', },
        'KEY_PREFIX': 'matejalasanca', }, }

ALLOWED_HOSTS = [
    'mateja.lasan.ca',
    'www.mateja.lasan.ca',
    'mateja-lasan-ca.herokuapp.com', ]
