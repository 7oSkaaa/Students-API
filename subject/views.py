from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.forms import model_to_dict
from django.views import View
from .models import Subject
from .forms import SubjectForm
import json

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)
        return super().default(o)

def toJson(Subject):
    return json.loads(json.dumps(Subject, cls=ExtendedEncoder))

class SubjectView(View):

   # GET all subjects
    def get(self, request):
        subjects = Subject.objects.all()
        if subjects:
            return JsonResponse({'subjects': list(subjects.values())}, safe=False)
        else:
            return JsonResponse({'message': 'No subjects found!'}, status=422)
            
    # POST a new Subject
    def post(self, request):
        try:
            form = SubjectForm(data=json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Subject created successfully!'})
            else:
                return JsonResponse({'message': 'Subject not created!'}, status=422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)
    
class SubjectViewId(View):
    
    # GET a Subject by id
    def get(self, request, *args, **kwargs):
        Subject = Subject.objects.get(id=kwargs['id'])
        if Subject:
            return JsonResponse({'Subject': toJson(Subject)}, safe=False)
        else:
            return JsonResponse({'message': 'Subject not found!'}, status=422)
    
    # PUT a Subject by id
    def put(self, request, *args, **kwargs):
        try:
            form = SubjectForm(data=json.loads(request.body), instance=Subject.objects.get(id=kwargs['id']))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Subject updated successfully!'})
            else:
                return JsonResponse({'message': 'Subject not updated!'}, status=422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)
    
    # DELETE a Subject by id
    def delete(self, request, *args, **kwargs):
        Subject = Subject.objects.filter(id=kwargs['id'])
        if Subject:
            Subject.delete()
            return JsonResponse({'message': 'Subject deleted successfully!'})
        else:
            return JsonResponse({'message': 'Subject not found!'}, status=404)