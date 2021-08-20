import django_on_heroku
import os
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(env_variable)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_value('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_value('DEBUG') == 'True'

ADMINS = [('Ochom', 'ochomrichard752@gmail.com')]

ALLOWED_HOSTS = get_env_value('ALLOWED_HOSTS').split(" ")

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_extensions',  # use this to show_urls patterns
    'rest_framework.authtoken',
    'corsheaders',
    'rest_auth',
]

LOCAL_APPS = [
    'common',
    'accounts',
    'bugs',
    'records',
    'outpatient',
    'revenue',
    'laboratory',
    'radiology',
    'pharmacy',
    'inpatient',
    'organization',
    'inventory',
    'mpesa',
]

INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = get_env_value('AlLOWED_ORIGINS').split(" ")

ROOT_URLCONF = 'hosipoa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'accounts/templates')],
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

WSGI_APPLICATION = 'hosipoa.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(get_env_value('DATABASE_URL'),  conn_max_age=600)
}

if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': get_env_value('DB_NAME'),
            'USER': get_env_value('DB_USER'),
            'PASSWORD': get_env_value('DB_PASSWORD'),
            'HOST': get_env_value('DB_HOST'),
            'PORT': int(get_env_value('DB_PORT')),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER':
        'accounts.serializers.PasswordResetSerializer',
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_env_value('EMAIL_HOST')
EMAIL_USE_TLS = get_env_value('EMAIL_USE_TLS') == 'True'
EMAIL_PORT = int(get_env_value('EMAIL_PORT'))
DEFAULT_FROM_EMAIL = get_env_value('DEFAULT_FROM_EMAIL')
EMAIL_HOST_USER = get_env_value('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_value('EMAIL_HOST_PASSWORD')

django_on_heroku.settings(locals())
