from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    location = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
