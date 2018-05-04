from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	rut = models.CharField(max_length=10)

	def __str__(self):
		return self.user.__str__()
