"""
Django settings for gym_server project.

Generated by 'django-admin startproject' using Django 1.9c1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8iwd#2uq!*e_&qez%wp@wt2qy)qky$l)y9w+a5gjulieeib+s0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

SHARED_APPS = [

    'tenant_schemas',  
    'customers',

    'django.contrib.contenttypes',

    #'django.contrib.admin',
    'django.contrib.admin',
    'root_admin',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authtools',
    'rest_framework',
    'corsheaders',
    # gym users is here just for creating tables.
    # won't be used as shared.
    'gym_users'
]

TENANT_APPS = [
    
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',

    # your tenant-specific apps
    'django.contrib.admin',
    'tenant_admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'authtools',
    'rest_framework',
    'corsheaders',
    
    'gym_users',
    'gym_config',
    'gym_contents',
    'gym_clubs',
]    


INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]


MIDDLEWARE_CLASSES = [
    # django tenant taking control of our middleware ..
    'tenant_schemas.middleware.TenantMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gym_server.urls'

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

WSGI_APPLICATION = 'gym_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'gym',
        'USER' : 'gymuser',
        'PASSWORD' : 'S0M3L1KEiTH0t01'
    }
}

try:
    import localsettings
    DATABASES = localsettings.DATABASES
except:
    pass

    
################################################

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'authtools.User'

TENANT_MODEL = "customers.Client" 
PUBLIC_SCHEMA_URLCONF = 'gym_server.urls_public'
PUBLIC_SCHEMA_NAME = 'public'

# use hexxie.com that points back to locahost
SERVICE_MAIN_DOMAIN = 'hexxie.com'

CORS_ORIGIN_ALLOW_ALL = True
