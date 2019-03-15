from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'mateja-lasan-ca/static'


class MediaStorage(S3Boto3Storage):
    location = 'mateja-lasan-ca/media'
    file_overwrite = False
