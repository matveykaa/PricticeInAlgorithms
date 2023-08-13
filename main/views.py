from django.shortcuts import render, redirect, get_object_or_404
from .models import Task1, Task2
from .forms import Task1Form, Task2Form
import collections

def index(request):
    tasks1 = Task1.objects.order_by('-id')
    tasks2 = Task2.objects.order_by('-id')
    return render(request, 'main/index.html',{'title': 'Home', 'tasks1': tasks1, 'tasks2': tasks2})

def task1(request):
    error = ''
    if request.method == 'POST':
        form = Task1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Произошла ошибка'

    form = Task1Form()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'main/task1.html', context)


def task2(request):
    error = ''
    if request.method == 'POST':
        form = Task2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Произошла ошибка'

    form = Task2Form()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/task2.html', context)

def calculate1(request, task1_id):
    task = get_object_or_404(Task1, id=task1_id)
    a, b = task.words1.split(), task.words2.split()

    def is_universal(sub, super):
        freq_sub = collections.Counter(sub)
        freq_super = collections.Counter(super)
        for char, freq in freq_sub.items():
            if char not in freq_super or freq_super[char] < freq:
                return False
        return True

    universal_words = []
    for word1 in a:
        is_universal_for_all = all(is_universal(word2, word1) for word2 in b)
        if is_universal_for_all:
            universal_words.append(word1)

    res = ' '.join(universal_words)
    return render(request, 'main/res1.html', {'tasks1': task, 'res': res})

def calculate2(request, task2_id):
    task = get_object_or_404(Task2, id=task2_id)
    indices_list = []
    target = int(task.target)
    a = list(map(int, task.massiv.split()))
    num_to_index = {}
    for index, num in enumerate(a):
        complement = target - num
        if complement in num_to_index:
            indices_list.append(f'{num_to_index[complement]} {index}')
        num_to_index[num] = index

    if not indices_list:
        indices_list.append('No pair found')

    return render(request, 'main/res2.html', {'tasks2': task, 'indices_list': indices_list})

def delete1(request, task1_id):
    task = get_object_or_404(Task1, id=task1_id)
    task.delete()
    tasks = Task1.objects.order_by('-id')
    tasks2 = Task2.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Home', 'tasks1': tasks, 'tasks2': tasks2})

def delete2(request, task2_id):
    task = get_object_or_404(Task2, id=task2_id)
    task.delete()
    tasks = Task2.objects.order_by('-id')
    tasks1 = Task1.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Home', 'tasks1': tasks1,'tasks2': tasks})