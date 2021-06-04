"""
Django settings for django_web_app project.

Generated by 'django-admin startproject' using Django 2.1.7.

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
SECRET_KEY = '=m-e6oov5b2gv7o0af788&v5zgazj5-$x(67e$^tft^9y3-1x$'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

ALLOWED_HOSTS = ['hapay-faylopereday.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',# <-- https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
    #all auth [google]
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'django_web_app.urls'

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

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'django_web_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 2

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

MAX_UPLOAD_SIZE = 52428800 #50 MB max soze of file [x * 1024 * 1024]

# https://studygyaan.com/django/how-to-add-social-login-to-django
SOCIAL_AUTH_FACEBOOK_KEY = '457298425681347'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'e804e12084f6c31e253bb9d20de6ba4e'  # App Secret
#SOCIAL_AUTH_TWITTER_KEY = '9TD8f5fhasdsbf4w61GSM9' # залишу потомкам, хай єбуться з цим самі, мене заблочив твітер, виявляється не можна перепідв'язувати пошту з одного акаунту на інший :D )
#SOCIAL_AUTH_TWITTER_SECRET = 'mwtdcUe4uOvvjDk2Ausb45gsasdasdasashw65454TNSx'
SOCIAL_AUTH_GITHUB_KEY = 'ca6c4169d8ba86ccd48f'
SOCIAL_AUTH_GITHUB_SECRET = '53c40b7ee9c7bc3a512986c89967af765ee1e050'
# add google ouath in future and fix my twitter account(add email form old account)
# there may be an update/fix today :D

#captcha:
#html: 6LeDcoYaAAAAAH5sXXnvjlQ-F0hNrVKnnr8HrkeU
#code: 6LeDcoYaAAAAACgrY1SN-GuVF_jCZAnizneyUenh


#password reset: (See: https://support.google.com/accounts/answer/6010255?hl=en for details.)
#https://dev.to/yahaya_hk/password-reset-views-in-django-2gf2
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'IrisInMountains@gmail.com'  #<-----------------------
EMAIL_HOST_PASSWORD = 'Ares12345' #<-----------------------
EMAIL_USE_TLS = True

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
