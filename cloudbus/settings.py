import os
from pathlib import Path
import environ

# 1. Initialize Environment Variables
env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DJANGO_ALLOWED_HOSTS=(list, [])
)

BASE_DIR = Path(__file__).resolve().parent.parent

# Read .env file if it exists (for local development)
env_file = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# 2. Security Settings
# Pulls from Azure Portal 'App Settings'. If not found, uses the insecure default.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-5+!d14u)a3m2j!ivq09&fg5!#o=cl0=j=f(ky#u%0up1x^^a7q')

DEBUG = env('DJANGO_DEBUG', default=True)

# 3. FIXED ALLOWED HOSTS LOGIC
# This looks for the comma-separated string from Azure and turns it into a list
hosts_raw = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1')
ALLOWED_HOSTS = [h.strip() for h in hosts_raw.split(',')]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',
    'storages', # Azure Storage
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # For serving static files on Azure
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# 4. DATABASE CONFIGURATION (Pulls from Azure Portal Settings)
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': env('DB_NAME', default='buspassdb'),
        'USER': env('DB_USER', default='havilah22'),
        'PASSWORD': env('DB_PASSWORD', default='Oluwatobi_1111'),
        'HOST': env('DB_HOST', default='buspass-srv-oluwatobi.database.windows.net'),
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'encrypt': 'yes',
            'TrustServerCertificate': 'no',
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 5. STATIC & MEDIA FILES
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# WhiteNoise helps serve static files on Azure App Service
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Azure Blob Storage for Media (Optional)
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = env('AZURE_ACCOUNT_NAME', default='buspassstoragetobi')
AZURE_ACCOUNT_KEY = env('AZURE_ACCOUNT_KEY', default='')
AZURE_CONTAINER = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'