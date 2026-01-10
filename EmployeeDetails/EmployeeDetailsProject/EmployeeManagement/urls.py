from django.urls import path
from . import views

app_name = 'EmployeeManagement' 

urlpatterns = [
    path('update-delete/', views.updateDelete, name='updateDelete'),
]