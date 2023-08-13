from django.shortcuts import render, redirect, get_object_or_404
from .models import Task1, Task2
from .forms import Task1Form, Task2Form

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
    universal_words = []
    res = ''
    for word1 in a:
        is_universal = True
        for word2 in b:
            sub_idx = 0
            for char in word1:
                if sub_idx < len(word2) and word2[sub_idx] == char:
                    sub_idx += 1
            if sub_idx < len(word2):
                is_universal = False
                break

        if is_universal:
            universal_words.append(word1)
    for el in universal_words:
        res = res + ' ' + el
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