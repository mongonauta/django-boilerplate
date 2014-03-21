from .common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
import mongoengine

# MONGOENGINE
# http://staltz.github.io/djangoconfi-mongoengine/

SESSION_ENGINE = 'mongoengine.django.sessions' # OPTIONAL

_MONGODB_HOST = '127.0.0.1'
_MONGODB_USER = ''
_MONGODB_PASSWD = ''
_MONGODB_NAME = 'tea'

_MONGODB_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

