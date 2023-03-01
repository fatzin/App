from django import forms
#from .models import Links
import uuid

class FormLinks(forms.Form):
    link = forms.CharField(max_length=200)
    link_encurtado = forms.CharField(max_length=100)