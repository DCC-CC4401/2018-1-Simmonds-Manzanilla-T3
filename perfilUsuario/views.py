from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from espacios.models import ReservaEspacio
from articulos.models import ReservaArticulo

@login_required
def home(request):
    usuario = request.user
    if usuario.is_admin:
        redirect('landingPageAdmin')
    else:
        redirect('perfil')
        

@login_required
def informacionUsuario(request):
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

    if request.method == 'POST':
        articulos_a_eliminar=[]
        espacios_a_eliminar=[]
        for checkbox in request.POST:
            if 'espacio' in checkbox:
                numero = checkbox[7:]
                espacios_a_eliminar.append(numero)
            if 'articulo' in checkbox:
                numero = checkbox[8:]
                articulos_a_eliminar.append(numero)
        articulos_a_eliminar.sort(reverse=True)
        espacios_a_eliminar.sort(reverse=True)
        [ultimos_espacios_reservados[int(numero)].delete() for numero in espacios_a_eliminar]
        [ultimos_articulos_reservados[int(numero)].delete() for numero in articulos_a_eliminar]
    return render(request, 'perfilUsuario/perfilUsuario.html', context)
