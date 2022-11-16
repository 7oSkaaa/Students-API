from django.db import models
from parent.models import Parent
from django.core.exceptions import ValidationError


def validate_password(val):
    if len(val) < 8:
        raise ValidationError('Password must be at least 8 characters long')
    

class Account(models.Model):
    
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False, validators=[validate_password])
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name = 'account', null=False, blank=False)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'account'