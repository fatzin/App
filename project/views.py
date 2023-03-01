from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
#from .models import Links
from django.http import HttpResponse
from .forms import FormLinks
from django.shortcuts import redirect
from .models import FormLinks as Links
from django.views.generic import RedirectView
import qrcode


class PaginaInicial(TemplateView):
    template_name = 'home.html'

class UrlShort(View):
    http_method_names = ['post', 'get']
    template_name = 'url.html'
    form_class = FormLinks
    def get(self, request):
        form = self.form_class()
        status = request.GET.get('status')
        return render(request, self.template_name, {'form': form, 'status': status})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            link_encurtado = form.cleaned_data['link_encurtado']
            new_link = FormLinks(link=link, link_encurtado=link_encurtado)
            new_link.save()
            return redirect('success')
        return render(request, self.template_name, {'form': form})

class UrlCurta(View):
    http_method_names = ['post']
    template_name = 'urlcurta.html'
    def post(self, request):
          form = FormLinks(request.POST)
          link = form.data['link']
          link_encurtado = form.data['link_encurtado']
          links = Links.objects.filter(link_encurtado = link_encurtado)
          rendered_template = render(request, 'urlcurta.html', {'link': form.data['link_encurtado']})
          if len(links) > 0:
                return redirect("/url/?status=1")

          if form.is_valid():
            try:
                new_url = Links(link = link, link_encurtado = link_encurtado)
                new_url.save()
                img = qrcode.make(link)
                img.save(f'static/img/qrcode.png') 
                return HttpResponse(rendered_template)
            except:
                return HttpResponse(f"Erro interno do sistema")
      
class LinkRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        link = kwargs['link']
        links = Links.objects.filter(link_encurtado=link)
        if links.exists():
            return links[0].link
        else:
            return '/url'