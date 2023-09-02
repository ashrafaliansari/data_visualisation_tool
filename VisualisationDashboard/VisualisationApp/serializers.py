from rest_framework import serializers
from .models import JsonData

class JsonDataSlzr(serializers.ModelSerializer):
    class Meta:
        model = JsonData
        fields = ('end_year','intensity','sector','topic','insight','url','start_year','impact','added','published','country','relevance','pestle','source','title','likelihood')
