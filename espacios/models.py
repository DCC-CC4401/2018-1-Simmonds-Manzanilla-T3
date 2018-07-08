from django.db import models
from django.conf import settings


class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return self.nombre


class ReservaEspacio(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    autorizador = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
        on_delete=models.DO_NOTHING, limit_choices_to={'is_admin': True},
        related_name='maps')
    inicio = models.TimeField()
    fin = models.TimeField()
