from django.shortcuts import render

def index(request):
	pass

def landing_page_user(request):
	return render(request, 'app/landing_page_user.html')

def landing_page_admin(request):
	return render(request, 'app/landing_page_admin.html')
