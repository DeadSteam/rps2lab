import time  # Импорт модуля для работы с временем
import random  # Импорт модуля для генерации случайных чисел
import pytest  # Импорт Pytest для тестирования
from django.test import TestCase  # Импорт базового тестового класса Django
from .models import ArrayDB  # Импорт модели ArrayDB из вашего приложения


def generate_random_array(size=10):
    # Функция для генерации случайного массива заданного размера
    return [random.randint(1, 100) for _ in range(size)]


def add_arrays_to_database(num_arrays):
    # Функция для добавления массивов в базу данных с использованием bulk_create
    arrays = [ArrayDB(array_name="Array", array=generate_random_array()) for _ in range(num_arrays)]
    ArrayDB.objects.bulk_create(arrays)


# Определение класса тестов
class YourTestClass(TestCase):

    @pytest.mark.django_db
    def test_add_100_arrays(self):
        # Тест на добавление 100 массивов в базу данных
        start_time = time.time()  # Запоминаем время начала выполнения
        add_arrays_to_database(100)  # Вызываем функцию добавления массивов
        end_time = time.time()  # Запоминаем время окончания выполнения

        execution_time = end_time - start_time  # Рассчитываем время выполнения
        print(f"Тест 1 - Добавлено 100 массивов за {execution_time} секунд")
        self.assertEqual(ArrayDB.objects.count(), 100)  # Проверка, что в базе 100 массивов

    @pytest.mark.django_db
    def test_add_1000_arrays(self):
        # Тест на добавление 1000 массивов в базу данных
        start_time = time.time()
        add_arrays_to_database(1000)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Тест 2 - Добавлено 1000 массивов за {execution_time} секунд")
        self.assertEqual(ArrayDB.objects.count(), 1000)

    @pytest.mark.django_db
    def test_add_10000_arrays(self):
        # Тест на добавление 10000 массивов в базу данных
        start_time = time.time()
        add_arrays_to_database(10000)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Тест 3 - Добавлено 10000 массивов за {execution_time} секунд")
        self.assertEqual(ArrayDB.objects.count(), 10000)

    @pytest.mark.django_db
    def test_fetch_and_sort_arrays(self):
        # Тест на выгрузку и сортировку массивов из базы данных
        for num_arrays in [100, 1000, 10000]:
            add_arrays_to_database(num_arrays)

            start_time = time.time()
            arrays = ArrayDB.objects.values_list('array', flat=True)
            sorted_arrays = [sorted(arr) for arr in arrays]
            end_time = time.time()

            execution_time = end_time - start_time
            average_time_per_array = execution_time / num_arrays

            print(f"Тест - Выгрузка и сортировка {num_arrays} массивов завершены за {execution_time} секунд")
            print(f"Среднее время на один массив: {average_time_per_array} секунд")
            # Добавьте вашу логику успеха/неуспеха в соответствии с вашими требованиями

    @pytest.mark.django_db
    def test_clear_database(self):
        # Тест на очистку базы данных
        for num_arrays in [100, 1000, 10000]:
            add_arrays_to_database(num_arrays)

            start_time = time.time()
            ArrayDB.objects.all().delete()
            end_time = time.time()

            execution_time = end_time - start_time

            print(f"Тест - Очистка базы данных с {num_arrays} записями завершена за {execution_time} секунд")
            # Добавьте вашу логику успеха/неуспеха в соответствии с вашими требованиями
