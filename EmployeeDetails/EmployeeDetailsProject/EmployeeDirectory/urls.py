from django.urls import path 
from . import views

app_name = 'EmployeeDirectory' 

urlpatterns = [
    path('display/', views.display, name='display'),
]
