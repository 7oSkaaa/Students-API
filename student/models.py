from django.db import models
from parent.models import Parent
from django.core.validators import RegexValidator

validate_name = RegexValidator(regex='^[A-Z][a-zA-Z ]*$', message='Name must start with a capital letter and contain only letters')

class Student(models.Model):
    first_name = models.CharField(max_length=100, validators=[validate_name])
    last_name = models.CharField(max_length=100, validators=[validate_name])
    age = models.IntegerField()
    mark = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name = 'students')
    
    def __str__(self):
        return self.first_name
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']
        db_table = 'students'
        unique_together = [['first_name', 'last_name']]
        