from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from espacios.models import Espacio, ReservaEspacio
from datetime import datetime, date, time, timedelta


@login_required
def index(request):
    usuario_actual = request.user
    semanas = ["30/04/2018", "07/05/2018", "14/05/2018", "21/05/2018", "28/05/2018", "04/06/2018", "11/06/2018", "18/06/2018",
               "25/06/2018", "02/07/2018", "09/07/2018", "16/07/2018", "23/07/2018"]
    dia_hoy = datetime.today()
    for dia in semanas:
        if dia_hoy < datetime.strptime(dia, '%d/%m/%Y'):
            semana_inicio = datetime.strptime(dia_anterior, '%d/%m/%Y')
            break
        dia_anterior = dia
    semana_fin = semana_inicio + timedelta(days=5)
    reservas = ReservaEspacio.objects.filter(inicio__range=[semana_inicio, semana_fin]).order_by('inicio')
    context = {
        'usuario': usuario_actual,
        'reservas': reservas,
        'dia_hoy' : dia_hoy,
        'semana_inicio' : semana_inicio,
        'semana_fin' : semana_fin,
    }
    return render(request, 'index.html', context)

@login_required
def horario(request):
    usuario_actual = request.user
    context = {
        'usuario': usuario_actual,
    }
    return render(request, 'horario.html', context)

