from django.contrib import admin  # Импортируем класс admin из модуля django.contrib
from .models import ArrayDB  # Импортируем модель ArrayDB из текущего приложения

# Регистрируем модель ArrayDB в административной панели Django
admin.site.register(ArrayDB)
