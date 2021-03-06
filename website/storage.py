from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    custom_domain = settings.CDN_DOMAIN_NAME


class MediaStorage(S3Boto3Storage):
    location = 'media'
    custom_domain = settings.CDN_DOMAIN_NAME
    file_overwrite = False
