from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('newuser', views.newuser, name='newuser'),
	path('login', views.login_view, name='login'),
	path('login_succes', views.login_succes, name='login_succes'),
	path('logout', views.logout, name='logout'),
	path('logout_succes', views.logout_succes, name='logout_succes'),
]
