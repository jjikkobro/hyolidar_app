from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import lidar_view

app_name="lidar"

urlpatterns=[
    path("", lidar_view, name="lidarView")
]