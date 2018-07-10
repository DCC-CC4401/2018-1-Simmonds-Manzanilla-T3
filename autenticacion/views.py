from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from autenticacion.models import MyUser
from autenticacion.aceptacion import confirmar_validez
from django.contrib.auth.decorators import login_required


def index(request):
	return login_view(request)


def newuser(request):
	mensaje = ""
	mensajes = {
		'usuario' : "",
		'clave' : "",
		'clave2' : "",
		'nombre' : "",
		'rut' : "",
	}
	if request.method == 'POST':
		usuario = request.POST['usuario']
		clave = request.POST['clave']
		clave2 = request.POST['clave2']
		nombre = request.POST['nombre completo']
		rut = request.POST['RUT']
		aceptable, mensajes = confirmar_validez(usuario, nombre, rut, clave, clave2)
		if not aceptable:
			context = mensajes
			return render(request,'autenticacion/newuser.html', context)
		user = MyUser.objects.create_user(usuario, nombre, rut, clave)
		return render(request, 'autenticacion/index.html')
	#el uso de la siguiente variable es dudoso.
	context = {
		'mensaje' : mensaje
	}
	return render(request, 'autenticacion/newuser.html')


def login_view(request):
	mensaje = ""
	if request.method == 'POST':
		username = request.POST['usuario']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			# Redirect to a success page.
			if user.is_admin:
				#página a la que vá si es administrador.
				return redirect('landingPageAdmin')
				#return redirect('landing page admin')
			#página a la que vá si no es administrador.
			return redirect('perfil')
			#return redirect('landing page user')
		else:
			# Return an 'invalid login' error message.
			mensaje = "error al iniciar sesión"
	context = {
		'mensaje' : mensaje
	}
	return render(request, 'autenticacion/login.html', context)

@login_required
def logout_view(request):
	logout(request)
	return render(request,'autenticacion/logout_succes.html')
