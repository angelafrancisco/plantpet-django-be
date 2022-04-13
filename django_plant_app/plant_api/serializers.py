from rest_framework import serializers
from .models import Plant
from .models import Status


# serializers.ModelSerializer just tells django to convert sql to JSON
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        # tell django which model to use
        model = Plant  
        # tell django which fields to include
        fields = ('id', 'name', 'type', 'image', 'pot_size', 'room_name', 'direction', 'user_notes',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        # tell django which model to use
        model = Status
        # tell django which fields to include
        fields = ('id', 'plant', 'created_date', 'health', 'notes',)

