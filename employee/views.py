from django.shortcuts import render, redirect
from .forms import *
from .models import *

def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')

def add_employee(request):
    
    context = {
        'employee_form': EmployeeForm(),
        'error_message': ""
    }

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/employees')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', context)