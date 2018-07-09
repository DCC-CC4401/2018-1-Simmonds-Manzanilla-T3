from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from espacios.models import Espacio, ReservaEspacio


def index(request):
    return render(request, 'index.html', {})

@login_required
def horario(request):
    usuario_actual = request.user
    context = {
        'usuario': usuario_actual,
    }
    return render(request, 'horario.html', context)

