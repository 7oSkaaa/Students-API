from rest_framework import serializers
from .models import Parent
from student.models import Student

class StudentSerializerListInParent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name']

class ParentSerializer(serializers.ModelSerializer):
    
    students = StudentSerializerListInParent(many=True, read_only=True)
    
    class Meta:
        model = Parent
        fields = '__all__'
    