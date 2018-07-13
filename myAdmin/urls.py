from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingPageAdmin, name='landingPageAdmin'),
]
