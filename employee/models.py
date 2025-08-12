from django.db import models


class Employee(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    nic = models.CharField(max_length=12, unique=True)
    passport = models.CharField(max_length=8, unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], default='active')
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
