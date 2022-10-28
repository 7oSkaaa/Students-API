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
    
    def post(self, request):
        try:
            # get request data
            [username, password, parent_id] = [request.data['username'], request.data['password'], request.data['parent']] 
            
            # trying to get account by username and password
            account = Account.objects.get(username=username, password=password, parent = Parent.objects.get(id=parent_id))
            
            # generate token
            token = jwt.encode({'username': username, 'password': password, 'timestamp': datetime.timestamp(datetime.now())}, 'secret', algorithm='HS256')
            
            # generate token object
            newToken = {
                'token': token,
                'parent': Parent.objects.get(id=parent_id)
            }
            
            # save token in database
            Tokens.objects.create(**newToken)
            
            return Response({'token': token}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({'message': 'Parent not registered!'}, status=status.HTTP_404_NOT_FOUND)