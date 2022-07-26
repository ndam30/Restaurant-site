from datetime import datetime

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    order_time = models.DateTimeField(default=datetime.now, blank=True)
    address = models.CharField(max_length=100, null=Food)
    price = models.IntegerField()
    quantity = models.IntegerField()
    message = models.TextField()
    user_id = models.IntegerField(blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    name = models.CharField(max_length=200, null=True)


