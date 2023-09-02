from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import JsonData
from .resource import JsonResource
# Register your models here.
# class JsonAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     listData = ('end_year','intensity','sector','topic','insight','url','start_year','impact','added','published','country','relevance','pestle','source','title','likelihood')
class JsonAdmin(ImportExportModelAdmin):
    res_class=JsonResource

admin.site.register(JsonData,JsonAdmin)