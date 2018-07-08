from django.db import models
from django.conf import settings

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    foto = models.ImageField(upload_to='InventarioCEI/static/images', blank=True, null=True)

    DISPONIBLE = 'DIS'
    ENPRESTAMO = 'PRS'
    ENREPARACION = 'REP'
    PERDIDO = 'PER'
    ESTADO = (
        (DISPONIBLE, 'Disponible'),
        (ENPRESTAMO, 'En Prestamo'),
        (ENREPARACION, 'En Reparación'),
        (PERDIDO, 'Perdido'),
    )
    estado = models.CharField(
        max_length=3,
        choices=ESTADO,
        default=DISPONIBLE,
    )

    def __str__(self):
        return self.nombre + str(self.id)


class ReservaArticulo(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    autorizador = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
        on_delete=models.DO_NOTHING, limit_choices_to={'is_admin': True},
        related_name='map')
    entrega = models.DateTimeField()
    devolucion = models.DateTimeField()

    PENDIENTE = 'PEN'
    ACEPTADO = 'ACP'
    RECHAZADO = 'RCH'
    DEVUELTO = 'DEV'
    NODEVUELTO = 'NDV'
    ESTADO = (
    (PENDIENTE, 'Pendiente'),
    (ACEPTADO, 'Aceptado'),
    (RECHAZADO, 'Rechazado'),
    (DEVUELTO, 'Devuelto'),
    (NODEVUELTO, 'No devuelto'),
    )
    estado = models.CharField(
        max_length=3,
        choices=ESTADO,
        default=PENDIENTE,
    )
