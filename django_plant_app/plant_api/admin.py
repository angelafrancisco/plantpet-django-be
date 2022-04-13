from django.contrib import admin

# Register your models here.
from .models import Plant
from .models import Status
admin.site.register(Plant)
admin.site.register(Status)