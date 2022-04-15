from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    image = models.CharField(max_length=400, blank=True)
    size = models.PositiveIntegerField()
    room = models.CharField(max_length=32)
    DirectionChoices = models.TextChoices('DirectionChoices', 'North, South, East, West')
    direction = models.CharField(choices=DirectionChoices.choices, max_length=5)
    notes = models.CharField(max_length=100, blank=True)


class Status(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    HealthChoices = models.TextChoices('HealthChoices', 'Poor Good Excellent')
    health = models.CharField(choices=HealthChoices.choices, max_length=9)
    notes = models.CharField(max_length=100, blank=True)


class Task(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    schedule = models.PositiveIntegerField()
    due = models.DateField()
    completed = models.BooleanField(default=False)