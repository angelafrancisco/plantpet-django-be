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


class Status(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    # image = models.ImageField  # might start as url first
    HealthChoices = models.TextChoices('HealthChoices', 'Poor Good Excellent')
    health = models.CharField(choices=HealthChoices.choices, max_length=9)
    notes = models.CharField(max_length=30)


# class Water(models.Model):
#     plant = models.ForeignKey(Plant)
#     created_date = models.DateField()
#     # no. of days after create date until due
#     schedule = models.PositiveIntegerField()
#     due_date = models.DateField()
#     completed = models.BooleanField(default=False)