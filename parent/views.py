from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.forms import model_to_dict
from django.views import View
from .models import Parent
from .forms import ParentForm
import json

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)
        return super().default(o)

def toJson(Subject):
    return json.loads(json.dumps(Subject, cls=ExtendedEncoder))

class ParentView(View):

    # GET all parents
    def get(self, request):
        try:
            form = ParentForm(Parent.objects.all())
            return JsonResponse(toJson(form), safe=False)
        except:
            return JsonResponse({'message': 'No students found!'}, status=422)
            
    # POST a new parent
    def post(self, request):
        try:
            form = ParentForm(data=json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Parent created successfully!'})
            else:
                return JsonResponse({'message': 'Parent not created!'}, status=422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)       
    
class ParentViewId(View):
    
    # GET a parent by id
    def get(self, request, *args, **kwargs):
        try:
            form = ParentForm(Parent.objects.get(id=kwargs['id']))
            return JsonResponse({'student': toJson(form.data)})
        except:
            return JsonResponse({'message': 'Student not found!'}, status=422)
    
    # PUT a parent by id
    def put(self, request, *args, **kwargs):
        try:
            form = ParentForm(data=json.loads(request.body), instance=Parent.objects.get(id=kwargs['id']))
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Parent updated successfully!'})
            else:
                return JsonResponse({'message': 'Parent not updated!'}, status=422)
        except:
            return JsonResponse({'message': 'Format error!'}, status=422)

    # DELETE a parent by id
    def delete(self, request, *args, **kwargs):
        Parent = Parent.objects.filter(id=kwargs['id'])
        if Parent:
            Parent.delete()
            return JsonResponse({'message': 'Parent deleted successfully!'})
        else:
            return JsonResponse({'message': 'Parent not found!'}, status=422)