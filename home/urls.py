from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import get_status, home_view

app_name="home"

urlpatterns=[
    path('', home_view, name='home'),
    path('get-status/', get_status, name='get_status'),
]