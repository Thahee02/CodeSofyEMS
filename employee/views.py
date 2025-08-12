from django.shortcuts import render, redirect
from .forms import *
from .models import *

def hr_dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'hr_dashboard.html', {'employees': employees})

def add_employee(request):

    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/employees')
    else:
        form = EmployeeForm()

    context = {
        'employee_form': form,
        'error_message': ""
    }

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


def delete_employee(request, employee_id):
    if not request.user.is_authenticated:
        return redirect('/login')

    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('/employees')

def view_employee(request, employee_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    employee = Employee.objects.get(id=employee_id)

    context = {
        'employee': employee
    }

    return render(request, 'view_employee.html', context)
