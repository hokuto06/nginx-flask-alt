import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Puedes agregar rutas globales si querés
        'APP_DIRS': True,  # ✅ Esto le dice a Django que busque en app/templates/
        'OPTIONS': {
            'context_processors': [],
        },
    },
]


ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

# STATIC_URL = '/static/'   
FORCE_SCRIPT_NAME = '/django'
STATIC_URL = '/django/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
