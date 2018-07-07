from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from espacios.models import ReservaEspacio
from articulos.models import ReservaArticulo
@login_required
def informacionUser(request):
    usuario_actual = request.user
    ultimos_articulos_reservados = ReservaArticulo.objects.filter(usuario=usuario_actual).order_by('-devolucion')[:10]
    ultimos_espacios_reservados = ReservaEspacio.objects.filter(usuario=usuario_actual).order_by('-fin')[:10]
    context = {
        'usuario' : usuario_actual,
        'ultimos_articulos_reservados' : ultimos_articulos_reservados,
        'ultimos_espacios_reservados' : ultimos_espacios_reservados,

    }
    return render(request, 'perfilUser/reservasUsuario.html', context)
