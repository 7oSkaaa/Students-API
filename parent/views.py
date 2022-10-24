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
        parents = Parent.objects.all()
        if parents:
            return JsonResponse({'Parents': list(parents.values())}, safe=False)
        else:
            return JsonResponse({'message': 'No parents found!'}, status=404)
            
    # POST a new parent
    def post(self, request):
        form = ParentForm(data=json.loads(request.body))
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Parent created successfully!'})
        else:
            return JsonResponse({'message': 'Parent not created!'}, status=422)
    
    
class ParentViewId(View):
    
    # GET a parent by id
    def get(self, request, *args, **kwargs):
        Parent = Parent.objects.get(id=kwargs['id'])
        if Parent:
            return JsonResponse({'Parent': toJson(Parent)}, safe=False)
        else:
            return JsonResponse({'message': 'Parent not found!'}, status=404)
    
    # PUT a parent by id
    def put(self, request, *args, **kwargs):
        form = ParentForm(data=json.loads(request.body), instance=Parent.objects.get(id=kwargs['id']))
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Parent updated successfully!'})
        else:
            return JsonResponse({'message': 'Parent not updated!'}, status=422)
    
    # DELETE a parent by id
    def delete(self, request, *args, **kwargs):
        Parent = Parent.objects.filter(id=kwargs['id'])
        if Parent:
            Parent.delete()
            return JsonResponse({'message': 'Parent deleted successfully!'})
        else:
            return JsonResponse({'message': 'Parent not found!'}, status=404)