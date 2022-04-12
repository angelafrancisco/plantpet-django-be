from django.urls import path
from . import views

urlpatterns = [
    # api/plants will be routed to the PlantList view for handling
    path('', views.PlantList.as_view(), name='plant_list'),
    # api/plants will be routed to the PlantDetail view for handling
    path('<int:pk>', views.PlantDetail.as_view(), name='plant_detail'),
]