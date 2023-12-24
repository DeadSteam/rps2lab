from django import forms
from .models import ArrayDBS


class ArrayDBForm(forms.ModelForm):
    class Meta:
        model = ArrayDBS  # определяем, какая модель будет использоваться для создания формы
        fields = ('array_name', 'array')  # какие поля там будут
        widgets = {
            'array': forms.TextInput(attrs={'placeholder': 'Введите числа через запятую'}),
        }
