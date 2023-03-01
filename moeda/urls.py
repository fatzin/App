from django.urls import path
from . import views



urlpatterns = [
    path('moeda', views.MoedaView.as_view(), name='moeda'),
]
