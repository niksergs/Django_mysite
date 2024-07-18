import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Загрузка переменных окружения из .env.local
def load_env_file(filepath):
    with open(filepath) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value


load_env_file('.env.local')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG')))

ALLOWED_HOSTS = []

SITE_ID = 1     # Настроечный параметр для настройки карт сайтов

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'taggit',   # Приспособленное для использования приложение,
                # которое в первую очередь предлагает модель Tag и менеджер для удобного добавления тегов в любую модель
    'django.contrib.sites',     # Приложение для построения карт сайтов
    'django.contrib.sitemaps',  # Приложение для построения карт сайтов
    'django.contrib.postgres',  # PostgreSQL
    'social_django',            # Приложение для аутентификации через соцсети 'pip install social-auth-app-django'

    'blog',         # Основное приложение Блог
    'accounts',     # Приложение для регистрации
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # context_processors содержит список путей к вызываемым объектам,
                # которые возвращают словарь для объединения с контекстом каждого представления,
                # избавляя нас от необходимости добавлять одни и те же данные снова и снова.
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #   Ниже код для аутентификации через соцсети
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

"""Полный путь к каталогу, в котором хранятся загруженные файлы."""
MEDIA_ROOT = BASE_DIR/'media'

"""Базовый URL-адрес для обслуживания медиафайлов.
Это то, что позволяет нам получать доступ к мультимедиа через наш веб-браузер."""
MEDIA_URL = '/media/'

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

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

"""Сервера аутентификации (Дополнительно указаны сервера аутентификации через соцсети)"""
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

"""Аутентификация через соцсети - GitHub"""
SOCIAL_AUTH_GITHUB_KEY = os.environ.get('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('SOCIAL_AUTH_GITHUB_SECRET')

"""Аутентификация через соцсети - Google"""
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"    # Редирект после аутентификации

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # Истечение сессии через 30 дней

"""Настройки сервера электронной почты"""
"""Если вы не можете использовать SMTP-сервер, то можно сообщить Django, что нужно писать электронные письма в консоль,
добавив в файл settings.py следующий ниже настроечный параметр:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Конфигурация сервера электронной почты
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True