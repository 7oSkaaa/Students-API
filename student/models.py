from django import db
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthdate = models.DateField()
    class_number = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class meta:
        ordering = ['name']
        db_table = 'student'