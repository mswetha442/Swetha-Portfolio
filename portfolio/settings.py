import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security Settings for Production
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-ohvp=qvyx(_ede(!u$u@d!tm#t9+k^e#7smc$9dx2%$7%pl!r-')
DEBUG = os.environ.get('RENDER', 'False').lower() == 'false' and os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'main',
    
]
ROOT_URLCONF = 'portfolio.urls'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serves static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Note: WSGI_APPLICATION is set to portfolio.wsgi.application in your settings.
WSGI_APPLICATION = 'portfolio.wsgi.application'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Folder where your local custom static files live
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Path where Django will gather all static files for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Storage backend for WhiteNoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# Django 5.x Storage Configuration
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"