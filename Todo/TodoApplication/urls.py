from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsDone/<int:pk>/', views.markAsDone, name='markAsDone'),
    path('markAsUnDone/<int:pk>/', views.markAsUnDone, name='markAsUnDone'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
]