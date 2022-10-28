from rest_framework import mixins, generics, status
from rest_framework.response import Response

from parent.models import Parent
from .serializers import AccountSerializer
from .models import Account
from tokens.models import Tokens
from datetime import datetime
import jwt

class Register(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def post(self, request):
        return self.create(request)

class SignIn(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def put(self, request):
        try:
            token = jwt.encode({'username': request.data['username'], 'password': request.data['password'], 'timestamp': datetime.timestamp(datetime.now())}, 'secret', algorithm='HS256')
            newToken = {
                'token': token,
                'parent': Parent.objects.get(id=request.data['parent'])
            }
            Tokens.objects.create(**newToken)
            return Response({'token': token}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({'message': 'Parent not registered!'}, status=status.HTTP_404_NOT_FOUND)