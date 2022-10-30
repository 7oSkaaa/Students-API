from rest_framework import mixins, generics
from .serializers import ParentSerializer
from .middlewares import Authenticate
from .permissions import ParentPermissions, ParentDetailPermissions
from .models import Parent
from drf_yasg.utils import swagger_auto_schema

class ParentView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    # POST a new parent
    def post(self, request):
        return self.create(request)
    
    authentication_classes = [Authenticate]
    permission_classes = [ParentPermissions]
    
    # GET all parents
    @swagger_auto_schema(operation_description=
        """
            You must sent a token in the headers to access this endpoint
        """
    )
    def get(self, request):
        return self.list(request)
                    

class ParentDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    authentication_classes = [Authenticate]
    permission_classes = [ParentDetailPermissions]
    
    # GET a parent by id
    @swagger_auto_schema(operation_description=
        """
            You must sent a token in the headers to access this endpoint
        """
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # PUT a parent by id
    @swagger_auto_schema(operation_description=
        """
            You must sent a token in the headers to access this endpoint
        """
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # DELETE a parent by id
    @swagger_auto_schema(operation_description=
        """
            You must sent a token in the headers to access this endpoint
        """
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)