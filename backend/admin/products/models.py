from operator import mod
from statistics import mode
from turtle import title
from django.db import models



class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    likes=models.PositiveIntegerField(default=0)

class User(models.Model):
    pass