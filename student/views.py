from django.http import JsonResponse
from django.views import View
from .models import Student
import json

class StudentView(View):
    # GET all students
    def get(self, request):
        students = Student.objects.all()
        if students:
            return JsonResponse({'students': list(students.values())})
        else:
            return JsonResponse({'message': 'No students found!'})
    
    # POST a new student
    def post(self, request):
        student = json.loads(request.body)
        Student.objects.create(**student)
        return JsonResponse({'message': 'Student created successfully!'})

    
class StudentViewId(View):
    # GET a student by id
    def get(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs['id'])
        if student:
            return JsonResponse({'student': student})
        else:
            return JsonResponse({'message': 'Student not found!'})
    
    # PUT a student by id
    def put(self, request, *args, **kwargs):
        new_student = json.loads(request.body)
        old_student = Student.objects.filter(id=kwargs['id'])
        if old_student:
            old_student.update(**new_student)
            return JsonResponse({'message': 'Student updated successfully!'})
        else:
            return JsonResponse({'message': 'Student not found!'})
    
    # DELETE a student by id
    def delete(self, request, *args, **kwargs):
        student = Student.objects.filter(id=kwargs['id'])
        if student:
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully!'})
        else:
            return JsonResponse({'message': 'Student not found!'})