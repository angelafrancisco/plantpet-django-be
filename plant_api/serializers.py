from rest_framework import serializers
from .models import Plant
from .models import Status
from .models import Task

# serializers.ModelSerializer just tells django to convert sql to JSON
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        # tell django which model to use
        model = Plant  
        # tell django which fields to include
        fields = ('id', 'name', 'type', 'image', 'pot_size', 'room_name', 'direction', 'notes',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        # tell django which model to use
        model = Status
        # tell django which fields to include
        fields = ('id', 'plant', 'created_date', 'health', 'notes',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # tell django which model to use
        model = Task
        # tell django which fields to include
        fields = ('id', 'plant', 'created_date', 'schedule', 'due_date', 'completed',)
