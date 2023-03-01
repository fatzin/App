from django.http import HttpResponseNotAllowed
from django.urls import path
from . import views
from .views import PaginaInicial, UrlShort
from .views import RedirectView, UrlCurta

urlpatterns =[
    path('', PaginaInicial.as_view(), name = 'index'),
    path('url/', UrlShort.as_view(), name = 'urlshortener'),
    path('url/urlcurta/', views.UrlCurta.as_view(), name = 'urlcurta'),
    path('url/<str:link>/', views.LinkRedirectView.as_view(), name='link'),
]

