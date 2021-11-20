import os
from pathlib import Path
from datetime import timedelta 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r0n0n9tkdg7o@u%+80xp!fyt!5m_)yzsdv8flk_vr-=3sb=xew'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'appRestaurante',
]

# configuracion de como se deben generar los token cuando se este haciendo la autenticacion
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME'   : timedelta(minutes=5), # Tiempo de vida del token de acceso
    'REFRESH_TOKEN_LIFETIME'  : timedelta(days=1),    # Tiempo de vida del Refresh token
    'ROTATE_REFRESH_TOKENS'   : False,      # Rotacion de los token refresh
    'BLACKLIST_AFTER_ROTATION': False,       # que despues de que se hagan el refresh ese token no se vuelva a usar
    'UPDATE_LAST_LOGIN'       : False,
    'ALGORITHM'               : 'HS256',    # Se define el algoritmo de encriptacion de los token
    'USER_ID_FIELD'           : 'id',
    'USER_ID_CLAIM'           : 'user_id',
}

# Para que Django Rest-Framework pueda trabajar, le estamos dando permisos 
# y estamos verificando como se va a hacer autenticacion 
REST_FRAMEWORK = {
    # Permiso de Acceso 
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',# se da control total sobre las clases
    ),
    # Autenticacion de Acceso a esas Clases
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',# Mecanismo de Autenticacion por defecto
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apiRestaurante.urls'

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

WSGI_APPLICATION = 'apiRestaurante.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # conector de python a posgress
        'NAME': 'de4g0eb4f2fqcm',
        'USER': 'evjbaanysvncxl',
        'PASSWORD': 'a9ab8094204ec9c929eae55382e47210d969241158574fe476012762825e794b',
        'HOST': 'ec2-3-237-55-96.compute-1.amazonaws.com',
        'PORT': '5432'
    }
} """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'autenticacion',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# con esto tenemos acceso a las imagenes
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, '/media_root/')
STATIC_ROOT = '/static_root/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Modelo de Autenticacion y registro de Usuarios
AUTH_USER_MODEL = 'appRestaurante.UserProfile'
