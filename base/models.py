from django.db import models
from django.contrib.auth.models import User

class Customer_table(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
class Products_table(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class OrderingTable(models.Model):
    customer_name = models.CharField(max_length=50)
    product_id = models.ForeignKey(Products_table, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=50)

class Cart(models.Model):
    customer_name = models.CharField(max_length=50)  # Change customer_id to customer_name
    product = models.ForeignKey(Products_table, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ID: {self.id}, Customer: {self.customer_name}, Product: {self.product.product_name}"
    
class RewardsTable(models.Model):
    customer_name = models.CharField(max_length=100)
    rewards = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.customer_name} - {self.rewards} - {self.quantity}"