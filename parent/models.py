from django.db import models
from django.core.validators import RegexValidator


validate_name = RegexValidator(regex='^[A-Z][a-zA-Z ]*$', message='Name must start with a capital letter and contain only letters')

class Parent(models.Model):
    name = models.CharField(max_length=50, validators=[validate_name])
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'parents'