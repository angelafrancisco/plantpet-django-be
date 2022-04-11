from rest_framework import serializers
from .models import Plant


# serializers.ModelSerializer just tells django to convert sql to JSON
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        # tell django which model to use
        model = Plant  
        # tell django which fields to include
        fields = ('id', 'name', 'type', 'image', 'pot_size', 'room_name', 'direction', 'user_notes',)