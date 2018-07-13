from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

def confirmar_validez(usuario, nombre, rut, clave, clave2):
  aceptable=True	
  mensajemail=""
  mensajenombre=""
  mensajerut=""
  mensajeclave=""
  mensajeclave2=""
  #el usuario debe ser un correo válido.
  if not validateEmail(usuario):
    mensajemail="el correo no es válido."
    aceptable=False
  #el nombre da lo mismo. pero debe estar
  if not nombre:
    mensajenombre="debe tener nombre"
    aceptable = False
  #TODO el rut es un rut válido. no se como se ve de manera algorítmica,
  #así que se omite por ahora.
  #la clave debe ser válida.
  if not validatePassword(clave):
    mensajeclave="debe ingresar una clave."
    aceptable=False
  #las claves ingresadas deben las mísmas.
  if clave != clave2:
    mensajeclave2="las claves ingresadas deben ser iguales."
    aceptable=False
  mensajes = {
    'mensajeemail':mensajemail,
    'mensajenombre':mensajenombre,
    'mensajeclave':mensajeclave,
    'mensajeclave2':mensajeclave2,
  }
  return aceptable, mensajes

#función sacada de https://stackoverflow.com/questions/3217682/checking-validity-of-email-in-django-python, la primera respuesta.
def validateEmail( email ):
  try:
    validate_email( email )
    return True
  except ValidationError:
    return False

def validatePassword( password ):
  try:
    validate_password( password )
    return True
  except ValidationError:
    return False
