# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Employee Details Project!")

from django.shortcuts import render

from EmployeeDetailsApplication.models import Employee

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'home.html', context)