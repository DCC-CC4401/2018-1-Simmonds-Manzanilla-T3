from django.shortcuts import render
from django.http import HttpResponse
from horarioEspacios.models import Events
from espacios.models import Espacio, ReservaEspacio


def index(request):
    return render(request, 'index.html', {})


