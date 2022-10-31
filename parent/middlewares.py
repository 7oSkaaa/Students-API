from rest_framework import authentication, exceptions
from tokens.models import Tokens


class Authenticate(authentication.BaseAuthentication):
    def authenticate(self, request):
        # post request isn't necessary to authenticate
        if request.method == 'POST':
            return (True, None)
        # get the token from the headers
        sent_token = request.headers.get('Jwt')
        try:
            # get the token from the database
            token = Tokens.objects.get(token=sent_token)
            return (True, None)
        except Tokens.DoesNotExist:
            raise exceptions.AuthenticationFailed('You are not authenticated!')