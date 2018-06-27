from sentry.conf.server import *  # NOQA

import os

# ---- database ----

db_host = env('SENTRY_DB_HOST') or 'postgres'
db_name = env('SENTRY_DB_NAME') or 'sentry'
db_user = env('SENTRY_DB_USER') or 'sentry'
db_password = env('SENTRY_DB_PASSWORD') or ''
db_port = env('SENTRY_DB_PORT') or '5432'

DATABASES = {
    'default': {
        'ENGINE': 'sentry.db.postgres',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
        'OPTIONS': {
            'autocommit': True
        }
    }
}

# ---- redis ----

redis_host = env('SENTRY_REDIS_HOST') or 'redis'
redis_password = env('SENTRY_REDIS_PASSWORD') or ''
redis_port = env('SENTRY_REDIS_PORT') or '6379'
redis_db = env('SENTRY_REDIS_DB') or '0'

SENTRY_OPTIONS.update({
    'redis.clusters': {
        'default': {
            'hosts': {
                0: {
                    'host': redis_host,
                    'password': redis_password,
                    'port': redis_port,
                    'db': redis_db,
                },
            },
        },
    },
})

# ---- cache ----

memcached_host = env('SENTRY_MEMCACHED_HOST') or 'memcached'
memcached_port = env('SENTRY_MEMCACHED_PORT') or '11211'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [memcached_host + ':' + memcached_port],
        'TIMEOUT': 3600,
    }
}

# A primary cache is required for things such as processing events
SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

# ---- web ----

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    # 'workers': 3,  # the number of web workers
}

SENTRY_USE_BIG_INTS = True

secret_key = env('SENTRY_SECRET_KEY')

SENTRY_OPTIONS['system.secret-key'] = secret_key
