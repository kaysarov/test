import random
from django.shortcuts import render
from django.http import Http404
from .forms import MyForm, MyForm_1
import math


def base (request):
    return render(request, 'lab/base.html', {})


def rav(request, key):
    n = 100000
    max_st = 50
    form = MyForm(initial={'n': n, "m": max_st })
    name = 'X'
    res = []
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            max_st = form.cleaned_data['m']
    if key == 'random':
        title = 'Гистограмма равномерного распределения (Встроенная функция генерации случайных чисел Python)'
        for i in range(n):
            res.append([random.random()])
    elif key == 'kongr':
        title = 'Гистограмма равномерного распределения (Метод простых конгруэнций)'
        p = 2147483647
        a = 630360016
        x = 4
        for i in range(n):
            x = (a*x) % p
            res.append([x])
    elif key == 'lemer':
        title = 'Гистограмма равномерного распределения (Метод линейной конгруэнтной последовательности Лемара)'
        m = 10000
        a = 4001
        c = 39916801
        x = 0
        for i in range(n):
            x = (a*x+c) % m
            res.append([x])
    else:
        raise Http404

    return render(request, 'lab/histogram.html', {
        'mass': res,
        'title': title,
        'name': name,
        'max_st': max_st,
        'form': form,
    })


def treug (request):
    n = 100000
    max_st = 50
    z = 0
    h = 1
    form = MyForm_1(initial={'n': n, 'm': max_st, 'z': z, 'h': h})
    title = 'Гистограмма треугольного распределения'
    name = 'X'
    res = []
    a = 0
    b = 10
    if request.method == 'POST':
        form = MyForm_1(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            max_st = form.cleaned_data['m']
            h = form.cleaned_data['h']
            z = form.cleaned_data['z']
    for i in range(n):
        res.append([random.uniform(z/2+a/2*h, z/2+b/2*h) + random.uniform(z/2+a/2*h, z/2+b/2*h)])
    return render(request, 'lab/histogram.html', {
        'mass': res,
        'title': title,
        'name': name,
        'max_st': max_st,
        'form': form,
    })


def trap (request):
    n = 100000
    max_st = 50
    z = -7.5
    h = 1
    form = MyForm_1(initial={'n': n, 'm': max_st, 'z': z, 'h': h})
    title = 'Гистограмма трапецеидального распределения'
    name = 'X'
    res = []
    a = 30
    b = 60
    if request.method == 'POST':
        form = MyForm_1(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            max_st = form.cleaned_data['m']
            h = form.cleaned_data['h']
            z = form.cleaned_data['z']
    for i in range(n):
        res.append([random.uniform(z/2+h*a, z/2+h * (b - a) / 8) + random.uniform(z/2++h * (b - a) / 8, z/2++h * (b - a) / 4)])
    return render(request, 'lab/histogram.html', {
        'mass': res,
        'title': title,
        'name': name,
        'max_st': max_st,
        'form': form,
    })


def norm(request, key):
    n = 100000
    max_st = 50
    z = 0
    h = 1
    form = MyForm_1(initial={'n': n, 'm': max_st, 'z': z, 'h': h})
    res = []
    y = 12

    if request.method == 'POST':
        form = MyForm_1(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            max_st = form.cleaned_data['m']
            h = form.cleaned_data['h']
            z = form.cleaned_data['z']
    if key == 'norm':
        name = 'X'
        title = 'Гистограмма нормального распределения'
        for j in range(n):
            x = 0
            for i in range(y):
                x += random.random()
            res.append([z+h*(((12/y)**(1/2))*(x-y/2))])
    elif key == 'sravn':
        a = []
        b = []
        name = 'XY'
        title = 'Гистограмма нормального распределения (сравнение со встроенной функцией)'
        for j in range(n):
            x = 0
            for i in range(y):
                x += random.random()
            a.append(z+h*(((12/y)**(1/2))*(x-y/2)))
            b.append(random.gauss(z, h))
        for j, i in zip(a, b):
            res.append([j, i])
    else:
        raise Http404
    return render(request, 'lab/histogram.html', {
        'mass': res,
        'title': title,
        'name': name,
        'max_st': max_st,
        'form': form,
    })


def exp(request):
    n = 100000
    max_st = 50
    z = 0
    h = 1
    form = MyForm_1(initial={'n': n, 'm': max_st, 'z': z, 'h': h})
    title = 'Гистограмма экспоненциального распределения'
    name = 'X'
    res = []
    if request.method == 'POST':
        form = MyForm_1(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            max_st = form.cleaned_data['m']
            h = form.cleaned_data['h']
            z = form.cleaned_data['z']
    for i in range(n):
        res.append([z+(-1/h*math.log(random.random()))])
    return render(request, 'lab/histogram.html', {
        'mass': res,
        'title': title,
        'name': name,
        'max_st': max_st,
        'form': form,
    })


def giperexp(request):
    n = 100000
    max_st = 50
    z = 0
    h = 1
    form = MyForm_1(initial={'n': n, 'm': max_st, 'z': z, 'h': h})
    title = 'Гистограмма гиперэкспоненциального распределения'
    name = 'X'
    res = []
    if request.method == 'POST':
        form = MyForm_1(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            max_st = form.cleaned_data['m']
            h = form.cleaned_data['h']
            z = form.cleaned_data['z']
    for i in range(n):
        x = random.random()
        if x > 0.3:
            res.append([z+h*(-1/6*math.log(random.random()))])
        res.append([z+h*(-1/1*math.log(random.random()))])
    return render(request, 'lab/histogram.html', {
        'mass': res,
        'title': title,
        'name': name,
        'max_st': max_st,
        'form': form,
    })


def erl(request):
    n = 100000
    max_st = 50
    z = 0
    h = 1
    form = MyForm_1(initial={'n': n, 'm': max_st, 'z': z, 'h': h})
    title = 'Гистограмма эрлановского распределения'
    name = 'X'
    res = []
    if request.method == 'POST':
        form = MyForm_1(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            max_st = form.cleaned_data['m']
            h = form.cleaned_data['h']
            z = form.cleaned_data['z']
    for i in range(n):
        res.append([z+(-1/h*math.log(random.random()))+(-1/h*math.log(random.random()))])
    return render(request, 'lab/histogram.html', {
        'mass': res,
        'title': title,
        'name': name,
        'max_st': max_st,
        'form': form,
    })
