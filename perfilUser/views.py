from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def informacionUser(request):
    usuario_actual = request.user
    context = {
        'usuario' : usuario_actual,
    }
    return render(request, 'perfilUser/infoUsuario.html', context)
