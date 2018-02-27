from django import forms


class MyForm(forms.Form):
    n = forms.IntegerField(label='Введите количество случайных чисел')
    m = forms.IntegerField(label='Введите количество интервалов')


class MyForm_1(forms.Form):
    n = forms.IntegerField(label='Введите количество случайных чисел')
    m = forms.IntegerField(label='Введите количество интервалов')
    h = forms.FloatField(label='Введите коэффициент для изменения ширины гистограммы')
    z = forms.FloatField(label='Смещение по оси x')
