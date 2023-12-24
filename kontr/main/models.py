from django.db import models


class ArrayDBS(models.Model):
    array_name = models.CharField(max_length=100)  # так мы определяем текстовое поле с ограничением на количество символов.
    array = models.TextField()  # так определяется поле для неограниченно длинного текста

    class Meta:
        verbose_name = 'Массив'
        verbose_name_plural = 'Массивы'
