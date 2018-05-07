from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    foto = models.ImageField(upload_to='InventarioCEI/static/images', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10) # 12345678-0 -> 12.345.678-0
    foto = models.ImageField()
    isAdmin = models.BooleanField(default=False)
    reservas = models.ManyToManyField(Articulo)

    def __str__(self):
        return self.rut  # TODO: Retornar nombre y apellido de usuario
