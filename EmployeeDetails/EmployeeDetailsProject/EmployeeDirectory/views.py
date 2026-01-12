from django.shortcuts import render, get_object_or_404
from EmployeeManagement import models

# Create your views here.
def display(request):
    employees = models.Employee.objects.all()
    return render(request, "employeeDetails.html", {'employees': employees})

def displayEmployee(request, pk):
    employee = get_object_or_404(models.Employee, pk=pk)
    return render(request, "employeeDetail.html", {"employee": employee})
