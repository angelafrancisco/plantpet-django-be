from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    image = models.CharField(max_length=250)
    pot_size = models.PositiveIntegerField()
    room_name = models.CharField(max_length=32)
    direction = models.CharField(max_length=2)
    notes = models.CharField(max_length=100)


class Status(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    HealthChoices = models.TextChoices('HealthChoices', 'Poor Good Excellent')
    health = models.CharField(choices=HealthChoices.choices, max_length=9)
    notes = models.CharField(max_length=30)


class Task(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    schedule = models.PositiveIntegerField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)