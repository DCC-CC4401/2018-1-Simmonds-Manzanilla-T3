from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index),
    #path('', views.Articulo.as_view()),
]