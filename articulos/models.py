from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    foto = models.ImageField(upload_to='InventarioCEI/static/images', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    articulo = models.ForeignKey(Articulo)
    usuario = models.ForeignKey(User)
    entrega = models.DateTimeField()
    devolucion = models.DateTimeField()