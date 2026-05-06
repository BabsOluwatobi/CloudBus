import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY ---
SECRET_KEY = 'django-insecure-5+!d14u)a3m2j!ivq09&fg5!#o=cl0=j=f(ky#u%0up1x^^a7q'
DEBUG = True
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://cloudbus-f8b4hsfhe2b3fae5.southafricanorth-01.azurewebsites.net']

# --- APPS & MIDDLEWARE ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',
    'mozilla_django_oidc',  # OIDC App
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Use this exact line
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

# --- DATABASE (Azure SQL) ---
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

# --- AUTHENTICATION ---
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# --- MICROSOFT ENTRA ID (OIDC) SETTINGS ---
OIDC_RP_CLIENT_ID = '0e83ac06-4892-44b8-aa05-915f2d1bbfe7'
OIDC_RP_CLIENT_SECRET = 'ewc8Q~RgtLO6lKlqTU17YSulx1WrofEAIndRQdcx'
OIDC_RP_SIGN_ALGO = 'RS256'

OIDC_OP_AUTHORIZATION_ENDPOINT = "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize"
OIDC_OP_TOKEN_ENDPOINT = "https://login.microsoftonline.com/organizations/oauth2/v2.0/token"
OIDC_OP_USER_ENDPOINT = "https://graph.microsoft.com/oidc/userinfo"
OIDC_OP_JWKS_ENDPOINT = "https://login.microsoftonline.com/common/discovery/v2.0/keys"

OIDC_CREATE_USER = True
OIDC_STATE_CONTROL = True
OIDC_AUTHENTICATION_CALLBACK_URL = 'oidc_callback'

# --- REDIRECT LOGIC ---
# Standard users go to your custom login view
LOGIN_URL = 'login' 
LOGOUT_URL = 'home'

# Microsoft users (Admins) are sent to the Admin Dashboard upon success
LOGIN_REDIRECT_URL = '/admin/'
LOGOUT_REDIRECT_URL = '/'

# --- AZURE & HTTPS SECURITY ---
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

# --- STATIC & MEDIA ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Azure Blob Storage for Media
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = 'buspassstoragetobi'
AZURE_ACCOUNT_KEY = '06yQGRcMTCWw54Kj0ryDvtG8c3A9mjq4Wmb2ZcZNSjOYDsWPf/oRq5CCn8igg/TN9faSqU5ORgRv+AStiJKIfw=='
AZURE_CONTAINER = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'