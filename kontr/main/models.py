from django.db import models  # Импортируем класс models из модуля django.db


# Определяем модель данных ArrayDB, которая наследуется от models.Model
class ArrayDB(models.Model):
    array_name = models.CharField(
        max_length=100)  # Определяем текстовое поле array_name с ограничением на количество символов (максимум 100)

    array = models.TextField()  # Определяем поле для неограниченно длинного текста

    # Метод get_absolute_url возвращает URL объекта модели, используется, например, при редиректах
    def get_absolute_url(self):
        return f'/{self.id}'

    # Класс Meta предоставляет метаданные для модели
    class Meta:
        verbose_name = 'Массив'  # Устанавливаем человекочитаемое имя в единственном числе

        verbose_name_plural = 'Массивы'  # Устанавливаем человекочитаемое имя во множественном числе
