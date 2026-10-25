from django.urls import path 
from . import views

urlpatterns = [
    path('', views.employees_list, name='employees_list'),
    path('<int:pk>', views.employee_detail, name='employee_detail'),
]