from rest_framework import serializers
from .models import Account
class AccountSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(style={'input_type': 'text', 'placeholder': 'Username'})
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = Account
        fields = ['username', 'password', 'parent']