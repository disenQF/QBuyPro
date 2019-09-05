import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g-0c9#9=!*2v7%3j!8druvh7k&0dt(e6$bno+$@yqavxxczt3k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'goods',
    'order',
    'actives'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QBuyPro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'QBuyPro.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qbuydb',
        'HOST': '119.3.170.97',
        'PORT': 3307,
        'USER': 'root',
        'PASSWORD': 'root',
        'CHARSET': 'utf8'
    }

}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/m/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 缓存
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://119.3.170.97:6378/2'
    }
}

# 配置session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_NAME = 'qbuy_session_id'
SESSION_COOKIE_AGE = 604800  # 1周


# 配置日志
LOGGING = {
    'version': 1,
    'formatters':{
        'simple':{
            'format': '[%(asctime)s %(name)s] %(message)s',
            'datefmt': '%Y-%m-d %H:%M:%S'
        }
    },
    'handlers': {
        'out': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'DEBUG'
        },

        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'level': 'INFO',
            'filename': 'qbuy.log'
        }
    },
    'logger': {
        'django': {
            'handlers': ['out', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'qbuy': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# 配置Celery
CELERY_IMPORTS = ('', )