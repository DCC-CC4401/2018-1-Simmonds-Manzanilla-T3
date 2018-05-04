from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {}
	return render(request, 'autenticacion/index.html', context)


def logout(request):
	context = {}
	return render(request, 'autenticacion/logout.html', context)
