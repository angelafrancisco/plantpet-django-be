from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    image = models.CharField(max_length=32)
    pot_size = models.PositiveIntegerField()
    room_name = models.CharField(max_length=32)
    direction = models.CharField(max_length=2)
    user_notes = models.CharField(max_length=100)
