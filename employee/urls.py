from django.urls import path
from .views import *

urlpatterns = [
    path('', hr_dashboard, name='hr_dashboard'),
    path('add_employee/', add_employee, name='add_employee'),
    path('edit_employee/<int:employee_id>/', edit_employee, name='edit_employee'),
    path('delete_employee/<int:employee_id>/', delete_employee, name='delete_employee'),
    path('view_employee/<int:employee_id>/', view_employee, name='view_employee'),
]