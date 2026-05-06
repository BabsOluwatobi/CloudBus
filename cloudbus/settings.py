import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5+!d14u)a3m2j!ivq09&fg5!#o=cl0=j=f(ky#u%0up1x^^a7q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# We use the asterisk '*' so that ANY URL (including the Azure region-specific ones) is allowed.
ALLOWED_HOSTS = ['*']

# ADD THIS LINE:
CSRF_TRUSTED_ORIGINS = ['https://cloudbus-f8b4hsfhe2b3fae5.southafricanorth-01.azurewebsites.net']
# import os
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',
    # 'storages',
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



# settings.py

INSTALLED_APPS += [
    'mozilla_django_oidc', # Add this
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # Keep default
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend', # Add this
]

# Entra ID Configuration
OIDC_RP_CLIENT_ID = '0e83ac06-4892-44b8-aa05-915f2d1bbfe7'
OIDC_RP_CLIENT_SECRET = 'ewc8Q~RgtLO6lKlqTU17YSulx1WrofEAIndRQdcx'
TENANT_ID = '9f8c1089-4ee0-4268-b27d-81b1b52a408e'

# Add this missing endpoint
OIDC_OP_USER_ENDPOINT = "https://graph.microsoft.com/oidc/userinfo"

# Ensure these are still present and correct for Multitenant
OIDC_OP_AUTHORIZATION_ENDPOINT = "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize"
OIDC_OP_TOKEN_ENDPOINT = "https://login.microsoftonline.com/organizations/oauth2/v2.0/token"
OIDC_OP_JWKS_ENDPOINT = "https://login.microsoftonline.com/discovery/v2.0/keys"

# Critical for "everyone" to be able to join
OIDC_CREATE_USER = True

# Redirects
LOGIN_REDIRECT_URL = "/admin/"
LOGOUT_REDIRECT_URL = "/"

# Force Django to use HTTPS for OIDC redirects when on Azure
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# 1. Allow the session cookie to be sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# 2. Ensure the OIDC state is stored correctly in the session
OIDC_STATE_CONTROL = True

# 3. Add this if not already there (helps with Azure's proxy)
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"