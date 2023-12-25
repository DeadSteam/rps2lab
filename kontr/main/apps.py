from django.apps import AppConfig  # Импортируем класс AppConfig из модуля django.apps


# Определяем класс конфигурации приложения MainConfig
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Устанавливаем поле default_auto_field для указания типа автоматического поля
    name = 'main'  # Устанавливаем имя приложения
