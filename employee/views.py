from django.shortcuts import render, redirect
from .forms import *
from .models import *

def hr_dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'hr_dashboard.html', {'employees': employees})

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


def edit_employee(request, employee_id):

    if not request.user.is_authenticated:
        return redirect('/login')

    employee = Employee.objects.get(id=employee_id)

    context = {
        'employee_form': EmployeeForm(instance = employee),
        'error_message': ""
    }

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employees')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', context)