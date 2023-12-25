"""
Настройки Django для проекта "kontr".

Сгенерировано с помощью 'django-admin startproject' с использованием Django 4.2.8.

Для получения дополнительной информации об этом файле см.
https://docs.djangoproject.com/en/4.2/topics/settings/

Для полного списка настроек и их значений см.
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Построение путей внутри проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Быстрые настройки разработки - не подходит для production
# См. https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: Держите секретный ключ, используемый в продакшне, в тайне!
SECRET_KEY = 'django-insecure-xw^+nt-+#!aa44ks+mqvr&vwln98t^b1%5mu21k_*ynxl-c0!5'

# SECURITY WARNING: Не запускайте с отладочным режимом в продакшне!
DEBUG = True

ALLOWED_HOSTS = []

# Определение приложений
INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Промежуточное ПО
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневой URL-конфигурации
ROOT_URLCONF = 'kontr.urls'

# Шаблоны
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

# WSGI-приложение
WSGI_APPLICATION = 'kontr.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}

# Проверка пароля
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

# Международизация
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'

# Папка для статических файлов
staticfiles_DIRS = [
    BASE_DIR / "static"
]

# Тип поля первичного ключа по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
