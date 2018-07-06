from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from salas.models import ReservaSala
from articulos.models import ReservaArticulo
@login_required
def informacionUser(request):
    usuario_actual = request.user
    ultimos_articulos_reservados = ReservaArticulo.objects.filter(usuario=usuario_actual).order_by('-devolucion')[:10]
    ultimas_salas_reservadas = ReservaSala.objects.filter(usuario=usuario_actual).order_by('-fin')[:10]
    context = {
        'usuario' : usuario_actual,
        'ultimos_articulos_reservados' : ultimos_articulos_reservados,
        'ultimas_salas_reservadas' : ultimas_salas_reservadas,

    }
    return render(request, 'perfilUser/infoUsuario.html', context)
