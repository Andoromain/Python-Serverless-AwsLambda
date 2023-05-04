"""
Django settings for ProjetVrai project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os

from pathlib import Path
from django.conf.global_settings import STATICFILES_DIRS, STATIC_ROOT,\
    MEDIA_ROOT, MEDIA_URL
from test.test_regrtest import ROOT_DIR
import pymysql
import mimetypes
#import environ

#ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
#env = environ.Env()
#READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
#if READ_DOT_ENV_FILE:
#   env.read_env(str(ROOT_DIR / '.env'))


mimetypes.add_type("text/javascript",".js",True)
mimetypes.add_type("text/css",".css",True)
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=+%t%tuxqizf7!(hcdrcyk8(_=3um1^v$4(cdnpeeqfila!r9z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProjetVrai',
    #'storages',
    #'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'corsheaders.middleware.CorsMiddleware',    
    'django.middleware.common.CommonMiddleware', 
]

ROOT_URLCONF = 'ProjetVrai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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


TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

#CORS_ORIGIN_WHITELIST = [
#    'https://hnwzdww5dc.execute-api.us-east-1.amazonaws.com',
#    'https://django-ml.s3.amazonaws.com',
#]

CORS_ORIGIN_ALLOW_ALL=True

WSGI_APPLICATION = 'ProjetVrai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# community_app/settings.py

# Database
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf'),
        },
    }
}


sql_mode='STRICT_TRANS_TABLES'
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'projetDB',
    'USER': 'admin',
    'PASSWORD': '26787295',
    'HOST': 'projet-database.********.us-east-1.rds.amazonaws.com',
    'PORT': '3306',
  }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""

sql_mode='STRICT_TRANS_TABLES'
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'projetpy',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
  }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#TEMPLATES[0]['DIRS']=[os.path.join(BASE_DIR/"templates")]
# AWS_KEY = "***"
# AWS_SECRET ="*****"
# AWS_ACCESS_KEY_ID="***"
# AWS_SECRET_ACCESS_KEY="****"
# AWS_STORAGE_BUCKET_NAME = "django-ml"
# AWS_QUERYSTRING_AUTH = False
# _AWS_EXPIRY = 60 * 60 * 24 * 7
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_S3_REGION_NAME = "us-east-1"
# AWS_DEFAULT_REGION = "us-east-1"
# AWS_LOCATION = 'static'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)
# DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_FINDERS = [
 #   'django.contrib.staticfiles.finders.FileSystemFinder',
 #   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#]
#STATIC_URL = '/static/'
#STATICFILES_DIRS = [
 #   os.path.join (BASE_DIR / "assets")
#]
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


#MEDIA_ROOT =[os.path.join(BASE_DIR / 'imgMateriel')]
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

MEDIA_ROOT=os.path.join(BASE_DIR,'imgMateriel')

MEDIA_URL="/img/"

STATIC_URL = '/assets/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"assets")]


TEMPLATES[0]['DIRS']=[os.path.join(BASE_DIR,"templates")]
