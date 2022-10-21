from django.db import models
import json

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    age = models.IntegerField()
    class_number = models.IntegerField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class meta:
        ordering = ['name']
        db_table = 'student'