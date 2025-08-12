from django.urls import path
from .views import *

urlpatterns = [
    path('', hr_dashboard, name='hr_dashboard'),
    path('add_employee/', add_employee, name='add_employee'),
    path('edit_employee/<int:employee_id>/', edit_employee, name='edit_employee'),
]