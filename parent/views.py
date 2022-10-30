from rest_framework import mixins, generics
from .serializers import ParentSerializer
from .middlewares import Authenticate
from .permissions import ParentPermissions, ParentDetailPermissions
from .models import Parent
class ParentView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    # POST a new parent
    def post(self, request):
        return self.create(request)
    
    authentication_classes = [Authenticate]
    permission_classes = [ParentPermissions]
    
    # GET all parents
    def get(self, request):
        return self.list(request)
                    

class ParentDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    authentication_classes = [Authenticate]
    permission_classes = [ParentDetailPermissions]
    
    # GET a parent by id
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # PUT a parent by id
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # DELETE a parent by id
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)