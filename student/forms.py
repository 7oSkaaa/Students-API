from django import forms
from django.forms import ValidationError 
from .models import Student

# validate the age in the form
def validate_age(value):
    if value < 5:
        raise ValidationError('Age must be greater than 5')

# validate the mark in the form
def validate_mark(value):
    if value < 50:
        raise ValidationError('Mark must be greater than 50')

# create a form for the student model
class StudentForm(forms.ModelForm):
    mark = forms.IntegerField(validators=[validate_mark])
    age = forms.IntegerField(validators=[validate_age])
    
    class Meta:
        model = Student
        fields = '__all__'