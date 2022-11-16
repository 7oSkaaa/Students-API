from rest_framework import permissions
from parent.models import Parent
from .models import Parent
from school.settings import SECRET_KEY
import jwt

class ParentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        self.message = 'You only can see your own data!'
        if request.method == 'GET':
            return False
        self.message = 'This method is not allowed!'
    

class ParentDetailPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        sent_token = jwt.decode(request.headers.get('Jwt'), SECRET_KEY, algorithms=['HS256'])
        parent_id = Parent.objects.filter(account__username=sent_token['username'], account__password=sent_token['password']).first().id
        parent_to_access = Parent.objects.get(id=parent_id)
        if parent_to_access == obj:
            return True
        self.message = 'You only deal with your own data!'
        return False