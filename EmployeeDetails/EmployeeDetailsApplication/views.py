from django.shortcuts import get_object_or_404, render
from .models import Employee

# Create your views here.
def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employees_list.html', context)

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)