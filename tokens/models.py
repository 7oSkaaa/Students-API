from django.db import models
from parent.models import Parent

class Tokens(models.Model):
    token = models.CharField(max_length=200, null=False, blank=False)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name = 'tokens', null=False, blank=False)
    
    class Meta:
        db_table = 'Tokens'
