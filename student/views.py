from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
class StudentView(APIView):
    # GET all students
    def get(self, request):
        data = StudentSerializer(Student.objects.all(), many=True).data
        return Response(data, status=status.HTTP_200_OK)
            
    # POST a new student
    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Invalid Formatted Data!'}, status=status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):
    
    # GET a student by id
    def get(self, request, *args, **kwargs):
        try:
            serializer = StudentSerializer(Student.objects.get(id=kwargs['id']))
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    # PUT a student by id
    def put(self, request, *args, **kwargs):
        try:
            serializer = StudentSerializer(Student.objects.get(id=kwargs['id']), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found!'}, status=status.HTTP_404_NOT_FOUND)
    # DELETE a student by id
    def delete(self, request, *args, **kwargs):
        try:
            Student.objects.get(id=kwargs['id']).delete()
            return Response({'message': 'Student deleted!'}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found!'}, status=status.HTTP_404_NOT_FOUND)