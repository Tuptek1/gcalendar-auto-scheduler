from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import Task
from .forms import TaskForm

@login_required(login_url="/users/login/")
def task_list(request):
    task_type = request.GET.get('task_type', '')
    priority = request.GET.get('priority', '')


    tasks = Task.objects.filter(user=request.user).order_by('name')

    if task_type:
        tasks = tasks.filter(task_type=task_type)
    if priority:
        tasks = tasks.filter(priority=priority)
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks,})


@login_required(login_url="/users/login/")
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task' : task})


@login_required(login_url="/users/login/")
def task_add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the logged-in user
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_add.html', {'form': form})

@login_required(login_url="/users/login/")
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, mark_safe(f'Task "<strong>{task.name}</strong>" has been successfully deleted.'))
    print(f'Task "{task.name}" has been successfully deleted.')

    return redirect('tasks:task_list')


@login_required(login_url="/users/login/")
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_edit.html', {'form' : form, 'task': task})