from django.db import models

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'subjects'