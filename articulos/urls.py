from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='busquedaArticulos'),
    path('search', views.search, name='search'),
    
    #path('', views.Articulo.as_view()),
]
