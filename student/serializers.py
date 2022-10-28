from rest_framework import serializers
from rest_framework.serializers import ValidationError
from subject.models import Subject
from .models import Student

# validate the age
def validate_age(value):
    if value < 5:
        raise ValidationError('Age must be greater than 5')

# validate the mark
def validate_mark(value):
    if value < 50:
        raise ValidationError('Mark must be greater than 50')

# validate the parent
def validate_parent(self):
    if self['parent'].name != self['last_name']:
        raise ValidationError('Parent name must be the same as student last name')


class SubjectSerializerListInStudent(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ['name']

class StudentSerializer(serializers.ModelSerializer):
    
    mark = serializers.IntegerField(validators=[validate_mark])
    age = serializers.IntegerField(validators=[validate_age])
    subjects = SubjectSerializerListInStudent(many=True, required=False, read_only = True)
    
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'mark', 'subjects', 'parent']
        validators = [validate_parent]