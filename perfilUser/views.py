from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from espacios.models import ReservaEspacio
from articulos.models import ReservaArticulo


@login_required
def informacionUser(request):
    """ Vista de la pantalla de perfil de usuario, contiene la navbar,
        botones que redireccionan hacia la reserva de salas y
        a la reserva de artículos, y listados (ordenados por fecha)
        de los últimos 10 espacios reservados, así como los últimos 10
        artículos reservados, cada uno conteniendo el nombre del
        espacio (o artículo) y su descripcion."""
    usuario_actual = request.user
    ultimos_articulos_reservados = ReservaArticulo.objects.filter(
        usuario=usuario_actual).order_by('-devolucion')[:10]
    ultimos_espacios_reservados = ReservaEspacio.objects.filter(
        usuario=usuario_actual).order_by('-fin')[:10]
    context = {
        'usuario' : usuario_actual,
        'ultimos_articulos_reservados' : ultimos_articulos_reservados,
        'ultimos_espacios_reservados' : ultimos_espacios_reservados,

    }
    return render(request, 'perfilUser/reservasUsuario.html', context)
