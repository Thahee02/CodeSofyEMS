from django.urls import path
from .views import *

urlpatterns = [
    path('', hr_dashboard, name='hr_dashboard'),
    path('add_employee/', add_employee, name='add_employee'),
]