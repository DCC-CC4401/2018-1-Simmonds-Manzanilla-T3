from django.db import models
from django.conf import settings

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    foto = models.ImageField(upload_to='InventarioCEI/static/images', blank=True, null=True)
    estadoActual = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class ReservaArticulo(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entrega = models.DateTimeField()
    devolucion = models.DateTimeField()
