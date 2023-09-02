from import_export import resources 
from .models import JsonData
class JsonResource(resources.ModelResource):
     class Meta:
         model = JsonData