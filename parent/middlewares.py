from rest_framework import authentication
from rest_framework import exceptions
from tokens.models import Tokens


class Authenticate(authentication.BaseAuthentication):
    def authenticate(self, request):
        sent_token = request.headers.get('Jwt')
        for token_object in Tokens.objects.all():
            if token_object.token == sent_token:
                return (True, None)
        raise exceptions.AuthenticationFailed('You are not authenticated!')
    