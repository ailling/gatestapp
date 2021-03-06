# Django settings for gatestapp project.

import os
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SETTINGS_PATH = os.path.dirname(__file__)

# --------------------------------------------------
# PROFILER SETTINGS
# --------------------------------------------------
# note: make sure to have celery running by running:
# python manage.py celeryd -E --loglevel=info
DJP_SEND_ASYNC = False

# note: celery will display some warnings if you have DEBUG = True; you can ignore these


# credentials for djangoperformance.com demo account.
# demo account username / password = demo / demo
DJP_APP_NAME = 'testapp'
DJP_APP_USERNAME = 'testapp'
DJP_API_KEY = '5c4401cb367b98ebe55ffb8be1d4a1f689e8ba79'

USE_BUNDLED_ENDPOINT = False
PROFILE_QUERIES = False
PROFILE_BENCHMARKS = False
PROFILE_MEMCACHE_STATS = False
PROFILE_USER_ACTIVITY = False


DATABASE_URL = 'mysql://gatestapp:db$testapp1@djp.cbt0lkdu6iin.us-east-1.rds.amazonaws.com/gatestapp'
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

# --------------------------------------------------
# CACHE SETTINGS
# --------------------------------------------------
CACHE_BACKEND = 'file://%s/file_cache' % (SETTINGS_PATH,)

# uncomment this line to use python-memcached for the cache backend
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't3si#w-q&amp;m8^&amp;l^lv!1=u+ogd#qv672*ps3l4^vre$8u9s51sl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
    # uncomment this line to profile the entie client application (recommended)
    'gatestapp.gaclient.middleware.DJPClientMiddleware',
    
#    'gatestapp.gaclient.middleware.TestMiddleware',
    # middleware for site-wide caching
#    'django.middleware.cache.UpdateCacheMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'gatestapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'gatestapp.wsgi.application'

TEMPLATE_PATH = os.path.join(SETTINGS_PATH, 'templates')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'gatestapp.books',
    
    
    'gatestapp.gaclient',
    
    'kombu.transport.django',
    'djcelery',
)


# -----------------------------------------------------------
# CELERY CONFIGURATION
# -----------------------------------------------------------
BROKER_BACKEND = 'django'
BROKER_HOST = DATABASES['default']['HOST']
BROKER_USER = DATABASES['default']['USER']
BROKER_PASSWORD = DATABASES['default']['PASSWORD']

import djcelery
djcelery.setup_loader()



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
