from rest_framework import serializers
from .models import Parent
from student.models import Student

class StudentSerializerListInParent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name']

class ParentSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(style={'input_type': 'text', 'placeholder': 'Name'})
    students = StudentSerializerListInParent(many=True, required=False, read_only = True)
    
    class Meta:
        model = Parent
        fields = '__all__'
    
