from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
	return render(request, 'autenticacion/index.html')


def new_user(request):
	return render(request, 'autenticacion/new_user.html')


def loging(request):
	return render(request, 'autenticacion/loging.html')


def login_succes(request):
	return render(request, 'autenticacion/login_succes.html')


def logout(request):
	return render(request,'autenticacion/logout.html')


def logout_succes(request):
	return render(request, 'autenticacion/logout_succes.html')
