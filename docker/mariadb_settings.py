# Django settings for layerindex project.
#
# Based on settings.py from the Django project template
# Copyright (c) Django Software Foundation and individual contributors.

DEBUG = False
ALLOWED_HOSTS = ['*']

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'layerindex',                 # Or path to database file if using sqlite3 (full path recommended).
        'USER': 'oelayer',                    # Not used with sqlite3.
        'PASSWORD': 'oelayer',                # Not used with sqlite3.
        'HOST': 'mariadb',                     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Avoid specific paths (added by paule)
import os
BASE_DIR = os.path.dirname(__file__)

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
STATIC_ROOT = '/opt/layerindex/layerindex/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

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
SECRET_KEY = '740b3412-3aeb-4480-98a4-bc1530c0da8e'

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

# We allow CORS calls from everybody
CORS_ORIGIN_ALLOW_ALL = True
# for the API pages
CORS_URLS_REGEX = r'.*/api/.*';


# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + "/templates",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'layerindex.context_processors.layerindex_context',
            ],
        },
    },
]

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
    'layerindex',
    'registration',
    'reversion',
    'reversion_compare',
    'captcha',
    'rest_framework',
    'corsheaders',
    'django_nvd3'
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'layerindex.restperm.ReadOnlyPermission',
    ),
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%m:%S+0000',
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success',
    messages.INFO: 'alert-info',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Registration settings
ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_HOST = 'smtp.example.com'
DEFAULT_FROM_EMAIL = 'noreply@example.com'
LOGIN_REDIRECT_URL = '/layerindex'

# Full path to directory where layers should be fetched into by the update script
LAYER_FETCH_DIR = "/opt/layers"

# Base temporary directory in which to create a directory in which to run BitBake
TEMP_BASE_DIR = "/tmp"

# Fetch URL of the BitBake repository for the update script
BITBAKE_REPO_URL = "git://lxgit.wrs.com/bitbake"

# Core layer to be used by the update script for basic BitBake configuration
CORE_LAYER_NAME = "openembedded-core"

# Update records older than this number of days will be deleted every update
UPDATE_PURGE_DAYS = 30

# Remove layer dependencies that are not specified in conf/layer.conf
REMOVE_LAYER_DEPENDENCIES = True

# Always use https:// for review URLs in emails (since it may be redirected to
# the login page)
FORCE_REVIEW_HTTPS = False

# Settings for layer submission feature
SUBMIT_EMAIL_FROM = 'noreply@example.com'
SUBMIT_EMAIL_SUBJECT = 'OE Layerindex layer submission'

# RabbitMQ settings
RABBIT_BROKER = 'amqp://admin:mypass@rabbit:5672'
RABBIT_BACKEND = 'rpc://'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Used for fetching repo
PARALLEL_JOBS = "4"

# Full path to directory where rrs tools stores logs
TOOLS_LOG_DIR = ""

# Full path to directory to store logs for dynamically executed tasks
TASK_LOG_DIR = "/tmp/layerindex-task-logs"