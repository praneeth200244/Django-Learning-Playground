from django.shortcuts import render, redirect, get_object_or_404
from ToDoApplication import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

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

def editTask(request, pk):
    if request.method == "POST":
        task = get_object_or_404(models.Task, pk=pk)
        new_task = request.POST.get("task", "").strip()
        if new_task:
            task.task = new_task
            task.save()
        return JsonResponse({"task": task.task})
    return JsonResponse({"error": "Invalid request"}, status=400)