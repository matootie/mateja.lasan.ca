import os
import dj_database_url


from website.settings.common import *


SECRET_KEY = os.environ['DJANGO_KEY']
REDIS_URL = os.environ['REDIS_URL']

DEBUG = False
WSGI_APPLICATION = 'website.wsgi.production.application'

AWS_ACCESS_KEY_ID = os.environ['AWS_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET']
AWS_STORAGE_BUCKET_NAME = 'cdnl'
AWS_S3_ENDPOINT_URL = 'https://ams3.digitaloceanspaces.com'
AWS_S3_CUSTOM_DOMAIN = 'cdn.mateja.lasan.ca'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400', }
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = None
STATIC_URL = 'https://cdn.mateja.lasan.ca/%s/' % AWS_LOCATION
STATICFILES_STORAGE = 'website.storage.StaticStorage'
DEFAULT_FILE_STORAGE = 'website.storage.MediaStorage'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

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
    'mateja.lasan.ca', ]
