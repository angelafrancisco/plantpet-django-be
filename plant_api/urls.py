from django.urls import path
from . import views

urlpatterns = [
    # '/plants' will be routed to the PlantList view for handling
    path('api/plants/', views.PlantList.as_view(), name='plant_list'),
    # '/plants/id' will be routed to the PlantDetail view for handling
    path('api/plants/<int:pk>/', views.PlantDetail.as_view(), name='plant_detail'),
    path('api/status/', views.StatusList.as_view(), name='status_list'),
    path('api/status/<int:pk>/', views.StatusDetail.as_view(), name='status_detail'),
    # path('tasks/', views.TaskList.as_view(), name='task_list'),
    # path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
]