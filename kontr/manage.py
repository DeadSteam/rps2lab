#!/usr/bin/env python
"""
Командная утилита Django для административных задач.
"""

import os
import sys

def main():
    """Выполнение административных задач."""
    # Установка переменной среды 'DJANGO_SETTINGS_MODULE' для указания файла настроек Django.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kontr.settings')
    try:
        # Импорт и выполнение команды из командной строки Django.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Невозможно импортировать Django. Убедитесь, что он установлен и "
            "доступен в переменной среды PYTHONPATH. Забыли активировать виртуальное окружение?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
