from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import redirect
import urllib.parse
import urllib.request
import json

# Create your views here.
class WeatherView(View):
    http_method_names = ['post', 'get', 'POST', 'GET']
    template_name = 'weather.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        if request.method == 'POST':
            API_KEY = '4ac6985bd180ed1527b477a328e73ba0'
            city = request.POST['city']
            encoded_city = urllib.parse.quote_plus(city)
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+encoded_city+'&lang=pt_br&appid='+API_KEY+'&units=metric').read()
            list_data = json.loads(source)
            data = {
                "country_code" : str(list_data['sys']['country']),
                "coordinates" : str(list_data['coord']['lon'])+','+str(list_data['coord']['lat']),
                "temp" : str(list_data['main']['temp'])+' °C',
                "description" : list_data['weather'][0]['description'],
                "icon" : list_data['weather'][0]['icon'],
                "main" : str(list_data['weather'][0]['main']),
                "humidity" : str(list_data['main']['humidity']),
                "pressure" : str(list_data['main']['pressure']),
            }
            if data:
                return render(request, self.template_name, data)
            else:
                return redirect("/weather/?status=1")    