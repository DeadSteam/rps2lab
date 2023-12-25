"""
WSGI-конфигурация для проекта "kontr".

Экспортирует вызываемый WSGI-объект как переменную верхнего уровня с именем «application».

Для получения дополнительной информации об этом файле см.
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# Импорт операционной системы и WSGI-приложения Django
import os
from django.core.wsgi import get_wsgi_application

# Установка переменной окружения с настройками Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kontr.settings')

# Создание WSGI-приложения Django
application = get_wsgi_application()