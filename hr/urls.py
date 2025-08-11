from django.urls import path
from .views import *

urlpatterns = [
    path('', hrAuth, name='hrAuth'),
    path('logout/', hr_logout, name='hr_logout'),
]