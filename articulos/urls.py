from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='landingPageNaturales'),
    path('search', views.search, name='search'),
    path('ficha', views.ficha, name='ficha'),
]
