from django import forms  # Импортируем необходимые классы из модуля forms библиотеки Django
from .models import ArrayDB  # Импортируем модель ArrayDB из текущего приложения


# Определяем класс формы ArrayDBForm, который наследуется от forms.ModelForm
class ArrayDBForm(forms.ModelForm):
    class Meta:
        model = ArrayDB  # Указываем модель, с которой связана данная форма

        fields = ('array_name', 'array')  # Указываем поля модели, которые будут отображены в форме

        # Настраиваем виджеты для каждого поля формы, задавая атрибуты класса и плейсхолдеры
        widgets = {
            'array_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название массива'}),
            'array': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите числа и буквы через запятую'}),
        }
