from django.urls import path
from . import views

urlpatterns = [
    # api/plants will be routed to the PlantList view for handling
    path('api/plants', views.PlantList.as_view(), name='plant_list'),
    # api/plants will be routed to the PlantDetail view for handling
    path('api/plants/<int:pk>', views.PlantDetail.as_view(), name='plant_detail'),
]