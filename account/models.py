from django import db
from django.db import models
from parent.models import Parent

class Account(models.Model):
    
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name = 'account', null=False, blank=False)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'account'