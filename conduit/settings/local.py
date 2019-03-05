from .base import *  # noqa

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ORIGIN_WHITELIST = (
    '0.0.0.0:4000',
    'localhost:4000',
)