from django.shortcuts import render
from EmployeeManagement import models

# Create your views here.
def display(request):
    employees = models.Employee.objects.all()
    return render(request, "employeeDetails.html", {'employees': employees})
