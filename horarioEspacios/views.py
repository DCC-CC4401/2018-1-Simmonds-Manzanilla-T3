from django.shortcuts import render
from django.http import HttpResponse
from espacios.models import Espacio, ReservaEspacio


def index(request):
    return render(request, 'index.html', {})

def horario(request):
    return render(request, 'horario.html', {})

