from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('new_user', views.new_user, name='new_user'),
	path('loging', views.loging, name='loging'),
	path('login_succes', views.login_succes, name='login_succes'),
	path('logout', views.logout, name='logout'),
	path('logout_succes', views.logout_succes, name='logout_succes'),
]
