from rest_framework import serializers
from .models import Subject
from student.models import Student


class StudentSerializerListInSubject(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name']

class SubjectSerializer(serializers.ModelSerializer):
    
    students = StudentSerializerListInSubject(many=True, read_only=True)
    
    class Meta:
        model = Subject
        fields = '__all__'