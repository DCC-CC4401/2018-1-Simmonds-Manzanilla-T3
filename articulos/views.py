from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import articulos.models as models

class Articulo(View):
    def get(self,request,*args,**kwargs):
        mic = models.Articulo.objects.filter(nombre='micrófono1').first()
        arg = {
            'articulo':mic,
            'reservas':models.ReservaArticulo.objects.filter(articulo=mic)
        }
        return render(request,'articulos/ficha.html',arg)


def index(request):
    estados = models.Articulo.ESTADO
    context = {'estados':estados,}
    return render(request, 'articulos/landing.html', context)