from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('landing_page_user', views.landing_page_user, name='landing page user'),
	path('landing_page_admin', views.landing_page_admin, name='landing page admin'),
]
