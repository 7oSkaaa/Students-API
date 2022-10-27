from django.db import models
from student.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    students = models.ManyToManyField(Student, related_name='subjects', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'subjects'