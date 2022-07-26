from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.shortcuts import redirect, render

from first.models import Food


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    publication_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    fop = models.ForeignKey(Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body= models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  '%s . %s' %(self.name,self.fop.name)