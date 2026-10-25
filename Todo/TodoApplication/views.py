from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST.get('task').strip()
    if task:
        Task.objects.create(task=task)
    return redirect('home')

def markAsDone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markAsUnDone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    new_task = request.POST.get("task", "").strip()
    if new_task:
        task.task = new_task
        task.save(update_fields=["task"])

    return redirect("home")