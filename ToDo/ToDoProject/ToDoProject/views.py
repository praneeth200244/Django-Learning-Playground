from django.shortcuts import render
from ToDoApplication import models

def home(request):
    tasks = models.Task.objects.filter(is_completed=False).order_by('-updated_at')
    # tasks = models.Task.objects.all().order_by('updated_at') For ascending order

    completed_tasks = models.Task.objects.filter(is_completed=True).order_by('-updated_at')

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html', context)