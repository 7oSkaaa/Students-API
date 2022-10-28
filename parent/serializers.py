from rest_framework import serializers
from .models import Parent
from student.models import Student
from account.models import Account

class StudentSerializerListInParent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name']

class AccountSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Account
        fields = ['username', 'password']

class ParentSerializer(serializers.ModelSerializer):
    
    students = StudentSerializerListInParent(many=True, required=False, read_only = True)
    account = AccountSerializer()
    class Meta:
        model = Parent
        fields = '__all__'
    
