from django.urls import path 
from . import views

app_name = 'ToDoApplication'
urlpatterns = [
    path('add-task/', views.addTask, name='addTask'),
    path('mark-as-done/<int:pk>', views.markAsDone, name='markAsDone'),
    path('mark-as-undone/<int:pk>', views.markAsUndone, name='markAsUndone'),
    path('delete-task/<int:pk>', views.deleteTask, name='deleteTask'),
]