from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Account

def validate_password(valu):
    if len(valu) < 8:
        raise ValidationError('Password must be at least 8 characters long')

class AccountSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(style={'input_type': 'text', 'placeholder': 'Username'})
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'}, validators=[validate_password])

    class Meta:
        model = Account
        fields = ['username', 'password', 'parent']