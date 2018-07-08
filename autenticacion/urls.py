from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('newuser', views.newuser, name='newuser'),
	path('login_view', views.login_view, name='login_view'),
	path('login_succes', views.login_succes, name='login_succes'),
	path('logout_view', views.logout_view, name='logout_view'),
	path('logout_succes', views.logout_succes, name='logout_succes'),
]
