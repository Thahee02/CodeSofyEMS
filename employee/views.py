from django.shortcuts import render
from .forms import *
from .models import *

def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')

def add_employee(request):
    
    context = {
        'employee_form': EmployeeForm(),
    }

    return render(request, 'add_employee.html', context)