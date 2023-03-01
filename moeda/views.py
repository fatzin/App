from django.shortcuts import render
from django.views.generic import View

class MoedaView(View):
    http_method_names = ['post', 'get', 'POST', 'GET']
    template_name = 'moeda.html'
    def get(self, request):
        return render(request, self.template_name)