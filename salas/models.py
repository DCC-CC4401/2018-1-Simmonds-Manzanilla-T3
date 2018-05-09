from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    sala = models.ForeignKey(Sala)
    usuario = models.ForeignKey(User)
    inicio = models.TimeField()
    fin = models.TimeField()