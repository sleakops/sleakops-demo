# pylint: skip-file
from .base import *  # noqa
from .base import env


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = False
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = False
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

# Email
#  ------------------------------------------------------------------------------
# https://github.com/django-ses/django-ses#readme
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django_ses.SESBackend")


AWS_STORAGE_ENABLED = env.bool("DJANGO_AWS_STORAGE_ENABLED", default=False)

if AWS_STORAGE_ENABLED:
    # STORAGES
    # ------------------------------------------------------------------------------
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
    AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME", default="")
    AWS_DEFAULT_ACL = env(
        "DJANGO_AWS_DEFAULT_ACL", default="public-read"
    )

    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
    # AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
    # aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # STATIC
    # ------------------------
    STATICFILES_STORAGE = env("DJANGO_STATIC_STORAGE", default="storages.backends.s3boto3.S3StaticStorage")
    # MEDIA
    # ------------------------------------------------------------------------------
    DEFAULT_FILE_STORAGE = env("DJANGO_MEDIA_STORAGE", default="storages.backends.s3boto3.S3Boto3Storage")

