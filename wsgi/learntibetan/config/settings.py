"""
Django settings for learntibetan project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)
DB_HOST = os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT', '5432')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_USER = os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME', DB_USER)
DB_PASSWORD = os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD', DB_PASSWORD)


if ON_OPENSHIFT:
    import sys
    sys.path.append(os.path.join(REPO_DIR, 'libs'))
    import secrets
    SECRETS = secrets.getter(os.path.join(DATA_DIR, 'secrets.json'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = SECRETS['secret_key']
else:
    # Make this unique, and don't share it with anybody.
    SECRET_KEY = os.urandom(24).encode('hex')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'

from socket import gethostname
ALLOWED_HOSTS = [
    gethostname(), # For internal OpenShift load balancer security purposes.
    os.environ.get('OPENSHIFT_APP_DNS'), # Dynamically map to the OpenShift gear name.
    #'example.com', # First DNS alias (set up in the app)
    #'www.example.com', # Second DNS alias (set up in the app)
    'games.budismoclasico.org',
]


# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# GETTING-STARTED: change 'myproject' to your project name:
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if ON_OPENSHIFT:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'learntibetan',          # Or path to database file if using sqlite3.
        'USER': DB_USER,          # Not used with sqlite3.
        'PASSWORD': DB_PASSWORD,   # Not used with sqlite3.
        'HOST': DB_HOST,       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': DB_PORT,                # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LOCALE_PATHS = [
        os.path.join(BASE_DIR, 'core', 'locale'),
       ]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Initial data
FIXTURE_DIRS = (os.path.join(BASE_DIR, 'core', 'fixtures'),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'core', 'static'),)
STATIC_ROOT = os.path.join(WSGI_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
