import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5+!d14u)a3m2j!ivq09&fg5!#o=cl0=j=f(ky#u%0up1x^^a7q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# We use the asterisk '*' so that ANY URL (including the Azure region-specific ones) is allowed.
# ALLOWED_HOSTS = ['cloudbus-f8b4hsfhe2b3fae5.southafricanorth-01.azurewebsites.net']
import os
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Essential for Azure
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cloudbus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cloudbus.wsgi.application'

# DATABASE CONFIGURATION - HARDCODED
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'buspassdb',
        'USER': 'havilah22',
        'PASSWORD': 'Oluwatobi_1111',
        'HOST': 'buspass-srv-oluwatobi.database.windows.net',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'encrypt': 'yes',
            'TrustServerCertificate': 'no',
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# This ensures CSS/JS load correctly on Azure App Service
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# AZURE STORAGE - HARDCODED
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = 'buspassstoragetobi'
AZURE_ACCOUNT_KEY = '06yQGRcMTCWw54Kj0ryDvtG8c3A9mjq4Wmb2ZcZNSjOYDsWPf/oRq5CCn8igg/TN9faSqU5ORgRv+AStiJKIfw=='
AZURE_CONTAINER = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'