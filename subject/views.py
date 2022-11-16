from rest_framework import generics
from .serializers import SubjectSerializer
from .models import Subject

# this class for get all subjects, create new subject
class SubjectView(generics.ListAPIView, generics.CreateAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    
# this class for get, update and delete a subject by id
class SubjectDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    