from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PlantSerializer
from .models import Plant

class PlantList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer  # tell django what serializer to use

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer