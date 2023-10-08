from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm, TaskPhotoForm
from rest_framework import generics
from .models import Task, TaskPhoto
from .serializers import TaskSerializer, TaskPhotoSerializer


def all_task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assuming user is logged in
            task.save()
            return redirect('task_detail', task_id=task.id)  # Redirect to task detail page
    else:
        form = TaskForm()

    return render(request, 'tasks/task_create.html', {'form': form})



def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', task_id=task.id)  # Redirect to task detail page
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_edit.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')  # Redirect to task list page


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')  # Redirect to task list page after registration
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

def create_task_photo(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        form = TaskPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            task_photo = form.save(commit=False)
            task_photo.task = task
            task_photo.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskPhotoForm()

    return render(request, 'tasks/task_photo_create.html', {'form': form, 'task': task})

def delete_task_photo(request, task_id, photo_id):
    task_photo = TaskPhoto.objects.get(id=photo_id)
    task_photo.delete()
    return redirect('task_detail', task_id=task_id)







class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskPhotoListCreateView(generics.ListCreateAPIView):
    queryset = TaskPhoto.objects.all()
    serializer_class = TaskPhotoSerializer

class TaskPhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskPhoto.objects.all()
    serializer_class = TaskPhotoSerializer












