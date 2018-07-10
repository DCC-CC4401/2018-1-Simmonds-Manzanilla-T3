from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db.models import Count

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
    context = {'estados':estados,
               'top4':get_top4(),}
    return render(request, 'articulos/landing.html', context)

def search(request):
    if request.method == 'GET':
        art = request.GET.get('articulo')
        sta = request.GET.get('estado')
        query = models.Articulo.objects.filter(nombre__icontains=art)
        if sta != '0':
            print(sta)
            query = query.filter(estado=sta)
        estados = models.Articulo.ESTADO
        context = {'estados': estados,
                   'top4':get_top4(),
                   'search': query}
        return render(request, 'articulos/landing.html', context)

def ficha(request):
    if request.method == 'GET':
        art_id = request.GET.get('fichart')
        art = models.Articulo.objects.get(id=art_id)
        context = {'articulo': art,
                   'reservas': models.ReservaArticulo.objects.filter(articulo=art)}
        return render(request, 'articulos/ficha.html', context)


def get_top4():
    return models.Articulo.objects.annotate(counter=Count('reservaarticulo')).order_by("-counter")[:4]
