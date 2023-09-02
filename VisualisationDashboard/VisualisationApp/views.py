from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JsonDataSlzr
from .models import JsonData

class JsondataView(viewsets.ModelViewSet):
    serializer_class = JsonDataSlzr
    queryset = JsonData.objects.all()

# Create your views here.
