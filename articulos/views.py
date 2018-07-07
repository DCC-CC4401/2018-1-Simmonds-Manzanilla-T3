from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import articulos.models as models

class Articulo(View):
    def get(self,request,*args,**kwargs):
        models.Articulo.objects.all().delete()
        models.Articulo.objects.create(nombre='Pala',descripcion='La pala pa las plantitas')
        arg = {'articulo':models.Articulo.objects.filter(nombre='Pala').first()}
        return render(request,'articulos/ficha.html',arg)
