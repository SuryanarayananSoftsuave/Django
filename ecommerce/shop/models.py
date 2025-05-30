from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        related_name ='products',
        null = True 
    )
    discription = models.TextField(max_length=200,null=True,blank=True)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=7)
    is_available = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=7)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    password=models.CharField(max_length=30)

class Order(models.Model):
    Product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    address=models.TextField(max_length=100)
    phone = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    status=models.BooleanField(default=False)

