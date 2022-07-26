from datetime import datetime

from django.db import models

# Create your models here.
class Contact(models.Model):
    foods = models.CharField(max_length=200)
    food_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    phone = models.IntegerField()
    Contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    name= models.CharField(max_length=100)
    tak = models.IntegerField( null=False)
    def __str__(self):
        return self.name

class Reserve(models.Model):


    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    phone = models.IntegerField()
    tablename = models.ForeignKey(Table, on_delete=models.DO_NOTHING, null=True )
    reserve_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
