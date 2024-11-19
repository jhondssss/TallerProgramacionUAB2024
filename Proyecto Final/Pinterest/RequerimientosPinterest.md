Create

Enunciado 1: Creación de un Nuevo Perfil de Usuario en Pinterest
Desarrollar una función que permita a un usuario crear un nuevo perfil en Pinterest. La función debe solicitar:

Nombre completo: El nombre completo del usuario.
Dirección de correo electrónico: Un correo electrónico válido que será utilizado para el registro.
Contraseña: Una contraseña segura para el acceso al perfil.
Descripción personal: Una breve descripción que el usuario desee incluir en su perfil (opcional).
Imagen de perfil: Opción para subir una imagen de perfil (opcional).
La función debe validar que todos los campos requeridos estén correctamente llenos y que el correo electrónico no esté ya registrado en la base de datos. Si la validación es exitosa, se debe almacenar el nuevo perfil y confirmar su creación al usuario, redirigiéndolo a su nuevo perfil con un mensaje de bienvenida.

Enunciado 1: Creación de un Nuevo Tablero Desarrollar una función que permita al usuario crear un nuevo tablero en la aplicación. La función debe solicitar:

Nombre del tablero: Un título que describa el tablero.
Descripción del tablero: Un breve texto que explique el propósito del tablero.
Nombre del usuario: Indicar quién está creando el tablero.
La función debe almacenar el nuevo tablero y confirmar su creación al usuario.

Enunciado 2: Agregar un Nuevo Pin a un Tablero Desarrollar una función que permita al usuario agregar un nuevo pin a un tablero existente. La función debe solicitar:

ID del tablero: El identificador del tablero al que se desea agregar el pin.
Título del pin: Un título que describa el pin.
URL del contenido: El enlace de la imagen o video que representa el pin.
Descripción del pin: Un breve texto que explique el contenido del pin.
Nombre del usuario: Indicar quién está subiendo el pin.
La función debe almacenar el nuevo pin en el tablero correspondiente y confirmar su creación al usuario.

Enunciado 3: Creación de un Comentario en un Pin Desarrollar una función que permita a los usuarios agregar un comentario a un pin específico. La función debe solicitar:

ID del pin: El identificador del pin al que se desea agregar el comentario.
Nombre del usuario: Indicar quién está comentando.
Contenido del comentario: El texto del comentario que se desea agregar.
La función debe almacenar el nuevo comentario y confirmar su creación al usuario.

-READ-
Enunciado: Listado de Pines en Tableros de Pinterest

Enunciado 1 Desarrollar una función que simule la visualización de pines en un tablero específico dentro de la aplicación que simula Pinterest. Esta función debe mostrar:

Contenido del Tablero: El nombre y la descripción del tablero al que se están agregando pines.
Lista de Pines: Mostrar todos los pines asociados al tablero, incluyendo:
Título del pin: Indicar el título que describe el pin.
URL del contenido: Mostrar el enlace de la imagen o video que representa el pin.
Descripción del pin: Un breve texto que explique el contenido del pin.
Nombre del usuario que creó el pin: Indicar quién subió cada pin.
Fecha de creación del pin: Mostrar la fecha en que se creó el pin, siguiendo las mismas reglas de visualización que para los tableros (hora si es reciente, sólo fecha si es más antigua).
Número total de pines: Indicar cuántos pines hay en total para el tablero.
La función debe permitir al usuario ingresar el ID del tablero (ejemplo: "viajes2023") para ver los pines asociados y manejar el caso en que no existan pines en el tablero. Además, la aplicación debe presentar un menú por consola que permita al usuario navegar entre diferentes tableros y pines.

Visualización de Todos los Tableros de un Usuario Desarrollar una función que permita al usuario visualizar todos los tableros que ha creado. La función debe mostrar:

Enunciado 2 Lista de tableros: Mostrar todos los tableros asociados al usuario, incluyendo:
ID del tablero: Un identificador único para cada tablero.
Nombre del tablero: El título que describe el tablero.
Descripción del tablero: Un breve texto que explique el propósito del tablero.
Fecha de creación: Mostrar la fecha en que se creó el tablero.
La función debe permitir al usuario ingresar su nombre de usuario para ver la lista de sus tableros y manejar el caso en que no existan tableros.

Visualización de Pines por Categoría Desarrollar una función que permita al usuario visualizar todos los pines de una categoría específica. La función debe solicitar:

Enunciado 3 Categoría: El nombre de la categoría de la que se desean visualizar los pines (por ejemplo, "Viajes", "Comida", "Moda").
Lista de pines: Mostrar todos los pines asociados a la categoría, incluyendo:
Título del pin: Un título que describa el pin.
URL del contenido: El enlace de la imagen o video que representa el pin.
Nombre del usuario que creó el pin: Indicar quién subió cada pin.
Descripción del pin: Un breve texto que explique el contenido del pin.
La función debe manejar el caso en que no existan pines en la categoría seleccionada y permitir al usuario navegar fácilmente entre diferentes categorías.

Update
Enunciado 1: Actualización de un Tablero Desarrollar una función que permita al usuario actualizar la información de un tablero existente. La función debe solicitar:

ID del tablero: El identificador del tablero que se desea actualizar.
Nuevo nombre del tablero (opcional): Un nuevo título para el tablero.
Nueva descripción del tablero (opcional): Un nuevo texto que explique el propósito del tablero.
La función debe actualizar la información del tablero y confirmar los cambios al usuario.

Enunciado 2: Actualización de un Pin Desarrollar una función que permita al usuario actualizar un pin existente. La función debe solicitar:

ID del pin: El identificador del pin que se desea actualizar.
Nuevo título del pin (opcional): Un nuevo título para el pin.
Nueva URL del contenido (opcional): Un nuevo enlace de la imagen o video que representa el pin.
Nueva descripción del pin (opcional): Un nuevo texto que explique el contenido del pin.
La función debe actualizar la información del pin y confirmar los cambios al usuario.

Enunciado 3: Actualización de un Comentario Desarrollar una función que permita al usuario actualizar un comentario en un pin específico. La función debe solicitar:

ID del pin: El identificador del pin donde se encuentra el comentario.
ID del comentario: El identificador del comentario que se desea actualizar.
Nuevo contenido del comentario: El texto actualizado del comentario.
La función debe actualizar el comentario y confirmar los cambios al usuario.

Delete
Enunciado 1: Eliminación de un Tablero Desarrollar una función que permita al usuario eliminar un tablero existente. La función debe solicitar:

ID del tablero: El identificador del tablero que se desea eliminar.
La función debe eliminar el tablero y confirmar la eliminación al usuario, manejando el caso en que el tablero no exista.

Enunciado 2: Eliminación de un Pin Desarrollar una función que permita al usuario eliminar un pin de un tablero. La función debe solicitar:

ID del pin: El identificador del pin que se desea eliminar.
La función debe eliminar el pin y confirmar la eliminación al usuario, manejando el caso en que el pin no exista.

Enunciado 3: Eliminación de un Comentario Desarrollar una función que permita al usuario eliminar un comentario en un pin específico. La función debe solicitar:

ID del pin: El identificador del pin donde se encuentra el comentario.
ID del comentario: El identificador del comentario que se desea eliminar.
La función debe eliminar el comentario y confirmar la eliminación al usuario, manejando el caso en que el comentario no exista.


Ante cualquier duda consultar con el Docente/Auxiliar.