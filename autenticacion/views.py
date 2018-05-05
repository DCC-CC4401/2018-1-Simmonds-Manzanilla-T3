from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
	return render(request, 'autenticacion/index.html')


def newuser(request):
	
	return render(request, 'autenticacion/newuser.html')


def loging(request):
	mensaje = ""
	if request.method == 'POST':
		username = request.POST['usuario']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			# Redirect to a success page.
			return render(request, 'autenticacion/login_succes.html')
		else:
			# Return an 'invalid login' error message.
			mensaje = "error al iniciar sesión"
	context = {
		'mensaje' : mensaje
	}
	return render(request, 'autenticacion/loging.html', context)


def login_succes(request):
	return render(request, 'autenticacion/login_succes.html')


def logout(request):
	return render(request,'autenticacion/logout.html')


def logout_succes(request):
	return render(request, 'autenticacion/logout_succes.html')
