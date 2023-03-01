from django.urls import path
from . import views
from .views import WeatherView

urlpatterns = [
    path('weather', views.WeatherView.as_view(), name='weather'),
]
