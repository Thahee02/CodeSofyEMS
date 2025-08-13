from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db.models import Q
import openpyxl
from django.http import HttpResponse


def hr_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('/login')
    
    query = request.GET.get('q', '')  

    if query:
        employees = Employee.objects.filter(
            Q(id__iexact=query) |  
            Q(first_name__icontains=query) |  
            Q(last_name__icontains=query) |
            Q(nic__icontains=query)
        )
    else:
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


def employees_excel(request):
    
    if not request.user.is_authenticated:
        return redirect('/login')

    employees = Employee.objects.all()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Employees"

    headers = ['ID', 'First Name', 'Last Name', 'DOB', 'NIC', 'Passport', 'Mobile', 'Telephone', 'Email', 'Address', 'Status']
    ws.append(headers)

    for emp in employees:
        ws.append([
            emp.id,
            emp.first_name,
            emp.last_name,
            emp.dob.strftime('%Y-%m-%d') if emp.dob else '',
            emp.nic,
            emp.passport,
            emp.mobile,
            emp.telephone,
            emp.email,
            emp.address,
            emp.status,
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=employees.xlsx'

    wb.save(response)
    return response




