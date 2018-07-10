from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from espacios.models import ReservaEspacio
from articulos.models import ReservaArticulo
from autenticacion.models import MyUser

@login_required
def landingPageAdmin(request):
    """ Vista de la pantalla de perfil de usuario, contiene la navbar,
        botones que redireccionan hacia la reserva de salas y
        a la reserva de artículos, y listados (ordenados por fecha)
        de los últimos 10 espacios reservados, así como los últimos 10
        artículos reservados, cada uno conteniendo el nombre del
        espacio (o artículo) y su descripcion."""
    usuario_actual = request.user
    usuarios_no_admins = MyUser.objects.filter(is_admin=False)
    articulos_reservados = ReservaArticulo.objects.filter(estado=ReservaArticulo.PENDIENTE).order_by('-devolucion')[:50]
    espacios_reservados = ReservaEspacio.objects.filter(estado=ReservaArticulo.PENDIENTE).order_by('-fin')[:50]
    context = {
        'usuario' : usuario_actual,
        'users':usuarios_no_admins,
        'articulos_reservados' : articulos_reservados,
        'espacios_reservados' : espacios_reservados,
    }
    if request.method == 'POST':
        indices_reservas=[]
        if 'rechazar_articulos' in request.POST:
            for req in request.POST:
                if 'res_articulos' in req:
                    numero=int(req[13:])
                    indices_reservas.append(numero)
            indices_reservas.sort(reverse=True)
            for indice in indices_reservas:
                reserva_a_cambiar = articulos_reservados[indice]
                reserva_a_cambiar.estado = ReservaArticulo.RECHAZADO
                reserva_a_cambiar.save()
        if 'aceptar_articulos' in request.POST:
            for req in request.POST:
                if 'res_articulos' in req:
                    numero=int(req[13:])
                    indices_reservas.append(numero)
            indices_reservas.sort(reverse=True)
            for indice in indices_reservas:
                    reserva_a_cambiar = articulos_reservados[numero]
                    reserva_a_cambiar.estado = ReservaArticulo.ACEPTADO
                    reserva_a_cambiar.save()
        if 'aceptar_espacios' in request.POST:
            for req in request.POST:
                if 'res_espacios' in req:
                    numero=int(req[12:])
                    indices_reservas.append(numero)
            indices_reservas.sort(reverse=True)
            for indice in indices_reservas:
                    reserva_a_cambiar=espacios_reservados[numero]
                    reserva_a_cambiar.estado= ReservaEspacio.RECHAZADA
                    reserva_a_cambiar.save()
        if 'rechazar_espacios' in request.POST:
            for req in request.POST:
                if 'res_espacios' in req:
                    numero=int(req[12:])
                    indices_reservas.append(numero)
            indices_reservas.sort(reverse=True)
            for indice in indices_reservas:
                    reserva_a_cambiar=espacios_reservados[numero]
                    reserva_a_cambiar.estado= ReservaEspacio.ACEPTADA
                    reserva_a_cambiar.save()

    return render(request, 'myAdmin/landingPageAdmin.html', context)
