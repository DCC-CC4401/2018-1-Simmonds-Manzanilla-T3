# 2018-1-Simmonds-Manzanilla-T3

Requisitos que deben implementar en forma completa: 1-2, 4-5, 7-8, 12, 14-18, 23, 25-26, 28, 37-40, 51, 54-56.

## Requisitos generales:

- [x] 1. El sistema debe permitir que personas naturales creen cuentas en el sistema,
  solicitando su nombre, RUT, correo electrónico y una contraseña.

- [x] 2. Todo usuario debe autentificarse para acceder al sistema, usando el correo
  electrónico que tiene registrado en el sistema y su contraseña.

- [x] 4. El sistema debe considerar 2 tipos de usuarios: administrador y persona natural
  (estudiante, funcionario, etc.).

- [ ] 5. El sistema debe permitir que personas naturales realicen reservas de artículos.

- [ ] 7. El sistema debe llevar un historial de las reservas realizadas por una persona
  natural, registrándose el usuario, fecha y hora de la reserva.

- [ ] 8. El sistema debe llevar un historial de los préstamos autorizados por un
  administrador, registrándose el usuario, fecha y hora del préstamo.

- [ ] 12. La reserva de cualquier artículo debe realizarse al menos 1 hora antes de la
  fecha/hora de inicio del préstamo.

- [ ] 14. Solo se puede reservar artículos y espacios en días hábiles, en el horario 09:00 -
  18:00.

- [ ] 15. Cada artículo y espacio debe tener un identificador único en el sistema.


## Landing page para personas naturales:

- [ ] 16. El sistema debe permitir buscar artículos.

- [ ] 17. El sistema solo se debe mostrar los artículos que cumplen con los criterios de
  búsqueda especificados por el usuario. Inicialmente, deben considerar los
  siguientes criterios: identificador, nombre del artículo, rango de fechas y estado
  (disponible, en préstamo, en reparación, perdido).

- [ ] 18. El sistema debe mostrar una grilla con los horarios en que están reservadas los
  espacios administrados por el CEI.

## Perfil del usuario (vista por el dueño del perfil):

- [x] 23. El sistema debe mostrar el nombre, RUT y correo electrónico del usuario.

- [x] 25. El sistema debe mostrar si el usuario está habilitado para crear reservas y
  concretar préstamos.

- [x] 26. El sistema debe mostrar un listado de las últimas 10 reservas realizadas por el
  usuario, ordenados por fecha (más nuevos al inicio de la lista), indicando cuales
  están pendientes, cuales fueron rechazadas y cuales ya fueron concretadas.  

- [x] 28. El sistema deber permitir que el usuario marque una o más reservas pendientes
  y eliminarlas.

## Ficha de un artículo:

- [x] 37. El sistema debe mostrar la siguiente información para un artículo: nombre, foto,
  texto descriptivo y estado actual (disponible, en préstamo, en reparación,
  perdido).

- [x] 38. El sistema también debe mostrar un resumen de las fechas en las cuales ha sido
  reservado el artículo.

- [ ] 39. En el caso de los administradores, el sistema debe permitir gestionar la
  información de un artículo.

- [ ] 40. En el caso de una persona natural, el sistema debe permitirle al usuario indicar
  que quiere reservar el artículo, indicando el rango de fecha y horas del préstamo
  solicitado.

## Landing page para administradores:

- [ ] 51. El sistema debe mostrar una grilla con los horarios en que están reservadas los
  espacios administrados por el CEI.  

- [ ] 54. El sistema debe mostrar un listado de todas las reservas pendientes en el
  sistema, ordenados por fecha (más nuevos al inicio de la lista).

- [ ] 55. El sistema debe permitir que el administrador marque una o más reservas
  pendientes, pudiendo cambiar su estado a entregado o rechazado.

- [ ] 56. El sistema debe mostrar un listado de todas los préstamos en el sistema,
  ordenados por fecha (más nuevos al inicio de la lista). El sistema debe permitir
  filtrar los préstamos por estado (vigentes, caducados, perdidos).
