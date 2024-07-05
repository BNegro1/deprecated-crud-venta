from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ('Cliente', 'Cliente'),
        ('Administrador', 'Administrador'),
        ('Vendedor', 'Vendedor'),
        ('Bodeguero', 'Bodeguero'),
        ('Contador', 'Contador'),
    ])
    rut = models.CharField(max_length=12, blank=True, null=True)  # RUT para administradores

    def __str__(self):
        return self.username

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Pending')
    client_name = models.CharField(max_length=100)
    client_address = models.CharField(max_length=200)
    client_email = models.EmailField()

    def __str__(self):
        return f"Order {self.id} - {self.client_name}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], default='Pending')
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment {self.id} - {self.order.client_name}"

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending')
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Delivery {self.id} - {self.order.client_name}"
