from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PlantSerializer
from .serializers import StatusSerializer
from .models import Plant
from .models import Status

class PlantList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer  # tell django what serializer to use

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer

class StatusList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer  # tell django what serializer to use

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer
