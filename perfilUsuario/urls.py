from django.urls import path

from . import views

urlpatterns = [
	path('perfil', views.informacionUsuario, name='perfil'),
    ]
