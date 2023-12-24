from django.shortcuts import render, redirect
from .models import ArrayDBS
from .forms import ArrayDBForm


def gnome_sort(arr):
    i, size = 1, len(arr)
    while i < size:
        if i == 0 or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1


def index(request):
    return render(request, 'main/index.html', {' title ': ''})


def about(request):
    return render(request, 'main/about.html')


def inputs(request):
    return render(request, 'main/input.html')


def load(request):
    all_dbs = ArrayDBS.objects.all()
    return render(request, 'main/load.html', {'all_dbs': all_dbs})


def handwork(request):
    if request.method == 'POST':
        form = ArrayDBForm(request.POST)
        if form.is_valid():
            array_instance = form.save(commit=False)

            if 'save_original' in request.POST:
                # Логика для сохранения исходного массива
                array_instance.save()
            elif 'save_sorted' in request.POST:
                # Логика для сортировки массива гномьей сортировкой и сохранения
                original_array_str = array_instance.array
                if original_array_str:
                    original_array_str = ''.join(['0' if c.isalpha() else c for c in original_array_str])
                    # Преобразование строки в список чисел
                    numbers = [int(x) for x in original_array_str.split(',')]
                    # Применение гномьей сортировки
                    gnome_sort(numbers)
                    # Преобразование отсортированного списка обратно в строку
                    sorted_str = ','.join(map(str, numbers))
                    array_instance.array = sorted_str
                    array_instance.save()

            return redirect('loaddb')  # Или другой редирект, который вам нужен
    else:
        form = ArrayDBForm()

    return render(request, 'main/handwork.html', {'form': form})


def autowork(request):
    return render(request, 'main/autowork.html')
