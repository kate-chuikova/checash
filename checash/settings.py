"""
Django settings for checash project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# import raven

import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

TEST_RUNNER = 'checash.heroku_test_runner.HerokuDiscoverRunner'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'raven.contrib.django.raven_compat',
    'items.apps.ItemsConfig',
    'bill.apps.BillConfig',
    'promo.apps.PromoConfig',
    'user.apps.UserConfig',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'checash.urls'

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

WSGI_APPLICATION = 'checash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


if os.getenv('BUILD_ON_TRAVIS', None):

    SECRET_KEY = 'i1ry9wiyq)hs(6*ltq0lrj3(c+)0@4&i3k*80cv+2d&7*gm&-e'

    DEBUG = False

    TEMPLATE_DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'travis_ci_db',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': 5432
        }
    }

else:

    SECRET_KEY = 'fx)vc4wh5ov43y1lxw+&4%6bl6*+em4j$m&3lkfz(&q7nl82p('

    DEBUG = True

    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # },

            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': '3411340',
                'HOST': 'localhost',
                'PORT': '5432',
            }
    }


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
DATABASES['default']['TEST'] = {'NAME': DATABASES['default']['NAME']}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SENTRY_PUBLIC_KEY = 'e6e95f90373f4ab1a956841d0e093961'
SENTRY_SECRET_KEY = '4eb94ef2e95846f29c244f2500f6cc53'
SENTRY_PROJECT = '219148'

# RAVEN_CONFIG = {
#     'dsn': 'https://{}:{}@sentry.io/{}'.format(
#         SENTRY_PUBLIC_KEY, SENTRY_SECRET_KEY, SENTRY_PROJECT
#     ),
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     # 'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
#     'release': os.environ['HEROKU_SLUG_COMMIT']
#     # 'CELERY_LOGLEVEL': logging.INFO
# }

# client = raven.Client('https://{}:{}@sentry.io/{}'.format(
#     SENTRY_PUBLIC_KEY, SENTRY_SECRET_KEY, SENTRY_PROJECT
# ))
