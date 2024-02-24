"""
ASGI-конфигурация для проекта "kontr".

Этот файл используется для настройки ASGI (Asynchronous Server Gateway Interface) в Django.

Он экспортирует ASGI-вызываемое как переменную верхнего уровня с именем «application».

Дополнительную информацию об этом файле можно найти по адресу:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

# Получаем ASGI-приложение Django.
from django.core.asgi import get_asgi_application

# Устанавливаем переменную среды 'DJANGO_SETTINGS_MODULE' для указания файла настроек Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kontr.settings')

# Создаем ASGI-приложение.
application = get_asgi_application()
