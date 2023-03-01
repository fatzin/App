from django.db import models
import uuid
# Create your models here.

#class Links(models.Model):
  #  link_redirecionado = models.URLField()
   # link_encurtado = models.CharField(max_length=10, unique=True)

    #def __str__(self) -> str:
     #   return self.link_encurtado

class FormLinks(models.Model):
    link = models.CharField(max_length=200)
    link_encurtado = models.CharField(max_length=10, unique=True)

     