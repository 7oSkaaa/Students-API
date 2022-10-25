from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.forms import model_to_dict
from django.views import View
from .models import Student
from .forms import StudentForm
import json

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)
        return super().default(o)

def toJson(student):
    return json.loads(json.dumps(student, cls=ExtendedEncoder))

class StudentView(View):

   # GET all students
    def get(self, request):
        students = Student.objects.all()
        if students:
            return JsonResponse({'students': list(students.values())}, safe=False)
        else:
            return JsonResponse({'message': 'No students found!'}, status=422)
            
    # POST a new student
    def post(self, request):
        try:
            form = StudentForm(data=json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Student created successfully!'})
            else:
                return JsonResponse({'message': 'Student not created!'}, status=422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)
    
class StudentViewId(View):
    
    # GET a student by id
    def get(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs['id'])
        if student:
            return JsonResponse({'Student': toJson(student)}, safe=False)
        else:
            return JsonResponse({'message': 'Student not found!'}, status=422)
            
    # PUT a student by id
    def put(self, request, *args, **kwargs):
        try:
            form = StudentForm(data=json.loads(request.body), instance=Student.objects.get(id=kwargs['id']))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Student updated successfully!'})
            else:
                return JsonResponse({'message': 'Student not updated!'}, status=422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)
        
    # DELETE a student by id
    def delete(self, request, *args, **kwargs):
        student = Student.objects.filter(id=kwargs['id'])
        if student:
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully!'})
        else:
            return JsonResponse({'message': 'Student not found!'}, status=422)