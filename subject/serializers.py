from rest_framework import serializers
from .models import Subject
from student.models import Student

class StudentSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name']

class SubjectSerializer(serializers.ModelSerializer):
    
    students = StudentSerializerList(many=True, read_only=True)
    
    class Meta:
        model = Subject
        fields = '__all__'