from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Student
from parent.models import Parent
from subject.models import Subject

# validate the age in the form
def validate_age(value):
    if value < 5:
        raise ValidationError('Age must be greater than 5')

# validate the mark in the form
def validate_mark(value):
    if value < 50:
        raise ValidationError('Mark must be greater than 50')


class ParentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Parent
        fields = ['name']

class SubjectSerializerList(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ['name']

class StudentSerializer(serializers.ModelSerializer):
    
    price = serializers.IntegerField(validators=[validate_mark])
    age = serializers.IntegerField(validators=[validate_age])
    parent = ParentSerializer()
    subjects = SubjectSerializerList(many=True)
    
    class Meta:
        model = Student
        fields = '__all__'
    