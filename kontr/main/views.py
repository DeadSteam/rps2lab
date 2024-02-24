from django.shortcuts import render, redirect  # Импортируем функции для работы с веб-приложением Django

from .models import ArrayDB  # Импортируем модель ArrayDB из текущего приложения

from .forms import ArrayDBForm  # Импортируем форму ArrayDBForm из текущего приложения

from django.views.generic import DetailView, UpdateView,DeleteView  # Импортируем классы для представлений DetailView, UpdateView, DeleteView


# Класс для детального просмотра массива
class ArrayDetailView(DetailView):
    model = ArrayDB
    template_name = 'main/details_view.html'  # Имя шаблона для отображения
    context_object_name = 'arraydetail'  # Имя объекта контекста
    form_class = ArrayDBForm  # Используемая форма


# Класс для обновления массива
class ArrayUpdateView(UpdateView):
    model = ArrayDB
    template_name = 'main/handwork.html'  # Имя шаблона для отображения
    form_class = ArrayDBForm  # Используемая форма

    # Метод, вызываемый при успешной валидации формы
    def form_valid(self, form):
        array_instance = form.save(commit=False)
        original_array_str = array_instance.array

        # Извлечение и обработка массива, как и раньше
        if original_array_str:
            original_array_str = ''.join([c for c in original_array_str if not c.isalpha()])
            numbers = [int(x) for x in original_array_str.split(',') if x]

        # Сохранение исходного массива при запросе
        if 'save_original' in self.request.POST:
            arr_str = ','.join(map(str, numbers))
            array_instance.array = arr_str
            return super().form_valid(form)

        # Сохранение отсортированного массива при запросе
        elif 'save_sorted' in self.request.POST:
            gnome_sort(numbers)
            sorted_str = ','.join(map(str, numbers))
            array_instance.array = sorted_str
            return super().form_valid(form)

        return super().form_valid(form)


# Класс для удаления массива
class ArrayDeleteView(DeleteView):
    model = ArrayDB
    success_url = '/indb'  # URL для перенаправления после успешного удаления
    template_name = 'main/delete.html'  # Имя шаблона для отображения


# Функция для сортировки массива гномьей сортировкой
def gnome_sort(arr):
    i, size = 1, len(arr)
    while i < size:
        if i == 0 or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1


# Функция для отображения главной страницы
def index(request):
    return render(request, 'main/index.html', {'title': ''})  # Отображение шаблона с передачей данных в контекст


# Функция для отображения страницы "О нас"
def about(request):
    return render(request, 'main/about.html')  # Отображение шаблона


# Функция для отображения страницы "Ввод"
def inputs(request):
    return render(request, 'main/input.html')  # Отображение шаблона


# Функция для отображения страницы "Загрузка"
def load(request):
    all_dbs = ArrayDB.objects.all()
    return render(request, 'main/load.html', {'all_dbs': all_dbs})  # Отображение шаблона с передачей данных в контекст


# Функция для отображения страницы "Ручная работа"
def handwork(request):
    if request.method == 'POST':
        form = ArrayDBForm(request.POST)
        if form.is_valid():
            array_instance = form.save(commit=False)
            original_array_str = array_instance.array
            if original_array_str:
                # Удаление букв из строки
                original_array_str = ''.join([c for c in original_array_str if not c.isalpha()])
                # Преобразование строки в список чисел
                numbers = [int(x) for x in original_array_str.split(',') if x]
            if 'save_original' in request.POST:
                # Логика для сохранения исходного массива
                # Преобразование списка обратно в строку
                arr_str = ','.join(map(str, numbers))
                array_instance.array = arr_str
                array_instance.save()
            elif 'save_sorted' in request.POST:
                gnome_sort(numbers)
                # Преобразование отсортированного списка обратно в строку
                sorted_str = ','.join(map(str, numbers))
                array_instance.array = sorted_str
                array_instance.save()

            return redirect('loaddb')  # Или другой редирект, который вам нужен
    else:
        form = ArrayDBForm()

    return render(request, 'main/handwork.html', {'form': form})  # Отображение шаблона с передачей формы в контекст


# Функция для отображения страницы "В базе данных"
def indb(request):
    all_dbs = ArrayDB.objects.all()
    return render(request, 'main/indb.html', {'all_dbs': all_dbs})  # Отображение шаблона с передачей данных в контекст
