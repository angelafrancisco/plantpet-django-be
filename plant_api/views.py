from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PlantSerializer
from .serializers import StatusSerializer
# from .serializers import TaskSerializer
from .models import Plant
from .models import Status
# from .models import Task

class PlantList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer  # tell django what serializer to use

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer

class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer

# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all().order_by('id')
#     serializer_class = TaskSerializer

# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all().order_by('id')
#     serializer_class = TaskSerializer
