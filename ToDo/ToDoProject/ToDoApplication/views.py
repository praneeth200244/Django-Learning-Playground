from django.shortcuts import render, redirect, get_object_or_404
from ToDoApplication import models


# Create your views here.
def addTask(request):
    # Handle POST request to add a new task
    if request.method == 'POST':
        task = request.POST.get('addTask')
        if task:
            models.Task.objects.create(task=task)
    return redirect('home')


def markAsDone(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markAsUndone(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def deleteTask(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.delete()
    return redirect('home')