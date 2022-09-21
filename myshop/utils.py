from storages.backends.s3boto3 import S3BotoStorage

MediaRootS3BotoStorage = lambda: S3BotoStorage(location='/myshop/media')