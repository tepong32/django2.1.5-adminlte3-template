"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1c+8^x7vj_@faa2h3**o1!er$9n+bx1dn@*0p&%hhtg6%kt0g2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    # third-party apps
    'adminlte3',
    'adminlte3_theme',
    'bootstrap_modal_forms',    # for forum topic and comment posting
    'crispy_forms',             # for better form-display formatting
    'ckeditor',
    'ckeditor_uploader',

    # custom
    'home.apps.HomeConfig',
    'blog.apps.BlogConfig',
    'user.apps.UserConfig',
    'freebie.apps.FreebieConfig',


    # django-allauth needs this
    'django.contrib.sites',
    # below are everything all-auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to allauth to enable:
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    # add more if you wish to
    
    # defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# django-allauth needs this
SITE_ID = 1

# edit this for customized ckeditor toolbar options
CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"
# CKEDITOR_CONFIGS = {
#     'awesome_ckeditor': {
#         'toolbar': 'Basic',
#     },
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': os.environ.get('GAUTH_CLIENTID'), # '960711795493-9vsgskaeg1qk3nc74qp27s9e7uoejitq.apps.googleusercontent.com'
            'secret': os.environ.get('GAUTH_SECRET'),      # '0-tHwlg4jvax1jt7p-JnvBmj'
            'key': ''
        }
    }
}

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

### PythonAnywhere DB settings for thehideout
# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': os.environ.get('DB_NAME'),
#     'USER': os.environ.get('DB_USER'),
#     'PASSWORD': os.environ.get('DB_PW'),    # hide this using env var
#     'HOST': 'thehideout.mysql.pythonanywhere-services.com',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")     # where we want django to save uploaded files
MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'     # for the css of crispy forms

LOGIN_REDIRECT_URL = 'home'     # needed for the login.html success instance
LOGIN_URL = 'login'             # for the @login_required decorator on user.views.profile

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # or only your domain name if you have your own mail server
EMAIL_PORT = 587 #587
EMAIL_USE_TLS = True


# TO USE THESE VARIABLES BELOW, USE ENVIRONMENT VARIABLES TO HIDE SENSITIVE INFO
# CHECK CoreyMs' Django TUTORIAL # 12 -- 14:20

EMAIL_HOST_USER = os.environ.get('ADMIN_EMAIL_UN') # var for email username
EMAIL_HOST_PASSWORD = os.environ.get('ADMIN_EMAIL_PW') # var for email pw
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # for email-sending pw-reset requests

