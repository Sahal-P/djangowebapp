import email
from pyexpat import model
from tkinter import Place
from turtle import position, title

from django.db import models

class position(models.Model):

    title= models.CharField(max_length=50)

class Person(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null = True)
    last_name = models.CharField(max_length=50,null = True)
    email = models.CharField(max_length=50,null = True)
    gender = models.CharField(max_length=50 ,null = True)
    position = models.ForeignKey(position, on_delete = models.CASCADE,null = True)
    # def __str__(self):
    #     return self.first_name


