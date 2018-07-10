from django.db import models
from django.conf import settings
from datetime import datetime


class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)

    DISPONIBLE = 'DIS'
    ENPRESTAMO = 'PRS'
    ENREPARACION = 'REP'
    ESTADO = (
    (DISPONIBLE, 'Disponible'),
    (ENPRESTAMO, 'En Prestamo'),
    (ENREPARACION, 'En Reparación'),
    )

    estado = models.CharField(
    max_length=3,
    choices=ESTADO,
    default=DISPONIBLE,
    )

    def __str__(self):
        return " espacio número " + str(self.id) + ": " + self.nombre


class ReservaEspacio(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    autorizador = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
        on_delete=models.DO_NOTHING, limit_choices_to={'is_admin': True},
        related_name='maps')
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    PENDIENTE = 'PEN'
    ACEPTADA = 'ACP'
    RECHAZADA = 'RCH'
    TERMINADA = 'TER'

    ESTADO = (
    (PENDIENTE, 'Pendiente'),
    (RECHAZADA, 'Aceptada'),
    (RECHAZADA, 'Rechazada'),
    (TERMINADA, 'Terminada'),
    )

    estado = models.CharField(
    max_length=3,
    choices=ESTADO,
    default=PENDIENTE,
    )

    def actualizar(self):
        if self.fin < datetime.now() and self.estado == ACEPTADA:
            self.estado=TERMINADA


    def __str__(self):
        return ("reserva de espacio número " + str(self.id) + ", usuario :" +
         str(self.usuario.email) + ", espacio: "+ str(self.espacio))
