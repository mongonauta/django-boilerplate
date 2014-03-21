import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '!^4_vs7b=pj4(0=gn@)qe=ie_%&)w$4f7fi38)73$3rcwv!3rw'

DEBUG = True

TEMPLATE_DEBUG = True

SITE_ID = 1

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': '',
    }
}

LANGUAGE_CODE = 'es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n'
)

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ( 
    os.path.join(BASE_DIR, '../static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "../media/")

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "../locale"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "../templates"),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}