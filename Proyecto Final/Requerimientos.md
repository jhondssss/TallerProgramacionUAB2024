Netflix

1. Create (Crear)
Requerimiento 1: El sistema debe permitir a los administradores agregar nuevos títulos de películas y series a la base de datos, incluyendo información como el título, género, año de lanzamiento, sinopsis, y la URL del tráiler. Esta operación debe validar que todos los campos requeridos estén completos antes de realizar la inserción en la base de datos.

Requerimiento 2: Los usuarios deben poder crear una cuenta en la plataforma proporcionando su nombre, dirección de correo electrónico, contraseña y preferencias de contenido. 

1. Read (Leer)
Requerimiento 1: El sistema debe permitir a los usuarios buscar y visualizar una lista de títulos disponibles en la plataforma, mostrando información básica como el título, género, y una breve descripción. (opcional: Esta información debe ser recuperada de la base de datos y presentada de manera paginada para mejorar la experiencia del usuario.)

Requerimiento 2: Los administradores deben poder acceder a un panel de control que les permita consultar estadísticas sobre el uso de la plataforma, como el número de usuarios activos, los títulos más vistos y las tendencias de visualización. Esta información debe ser extraída de la base de datos y presentada en un formato claro y comprensible.

3. Update (Actualizar)
Requerimiento 1: El sistema debe permitir a los administradores actualizar la información de los títulos existentes en la base de datos, incluyendo cambios en el género, año de lanzamiento, y sinopsis. La actualización debe ser registrada con un historial de cambios para mantener un registro de las modificaciones realizadas.

Requerimiento 2: Los usuarios deben poder actualizar su perfil, incluyendo cambios en su nombre, dirección de correo electrónico y preferencias de contenido. El sistema debe validar que la nueva dirección de correo electrónico no esté ya en uso por otro usuario antes de realizar la actualización en la base de datos.

4. Delete (Eliminar)
Requerimiento 1: El sistema debe permitir a los administradores eliminar títulos de la base de datos que ya no estén disponibles en la plataforma. Esta operación debe requerir una confirmación para evitar eliminaciones accidentales.

Requerimiento 2: Los usuarios deben tener la opción de eliminar su cuenta de la plataforma. Al realizar esta acción, el sistema debe solicitar una confirmación y, una vez confirmada, eliminar todos los datos asociados a la cuenta del usuario de la base de datos, asegurando que no queden registros residuales.

Starcraft

1. Create (Crear)
Requerimiento 1: El sistema debe permitir a los jugadores crear nuevas cuentas de usuario, proporcionando información como nombre de usuario, dirección de correo electrónico y contraseña. Esta información debe ser almacenada de manera segura en la base de datos y debe incluir validaciones para asegurar que el nombre de usuario sea único.

Requerimiento 2: Los administradores deben poder agregar nuevas unidades y estructuras al juego, incluyendo atributos como nombre, tipo, costo, estadísticas de combate y habilidades especiales. Esta información debe ser almacenada en la base de datos y estar disponible para su uso en el juego.

2. Read (Leer)
Requerimiento 1: Los jugadores deben poder acceder a un catálogo de unidades y estructuras disponibles en el juego, donde se muestre información detallada como estadísticas, habilidades y costo. Esta información debe ser recuperada de la base de datos y presentada de manera clara y accesible.

Requerimiento 2: Los administradores deben poder consultar estadísticas de juego, como el número de partidas jugadas, la cantidad de jugadores activos y las unidades más utilizadas. Esta información debe ser extraída de la base de datos y presentada en un formato visual, como gráficos o tablas.

3. Update (Actualizar)
Requerimiento 1: El sistema debe permitir a los jugadores actualizar su perfil, incluyendo cambios en su nombre de usuario, dirección de correo electrónico y preferencias de juego. El sistema debe validar que el nuevo nombre de usuario no esté ya en uso por otro jugador antes de realizar la actualización en la base de datos.

Requerimiento 2: Los administradores deben poder actualizar las estadísticas de las unidades y estructuras en el juego, ajustando atributos como daño, velocidad y costo. Cualquier cambio realizado debe ser registrado en un historial de cambios para mantener un registro de las modificaciones.

4. Delete (Eliminar)
Requerimiento 1: El sistema debe permitir a los administradores eliminar unidades o estructuras del juego que ya no sean relevantes o que necesiten ser reemplazadas. Esta operación debe requerir una confirmación para evitar eliminaciones accidentales.

Requerimiento 2: Los jugadores deben tener la opción de eliminar su cuenta del juego. Al realizar esta acción, el sistema debe solicitar una confirmación y, una vez confirmada, eliminar todos los datos asociados a la cuenta del jugador de la base de datos, asegurando que no queden registros residuales.

Whatsapp
1. Create (Crear)
Requerimiento 1: El sistema debe permitir a los usuarios crear nuevas cuentas de WhatsApp proporcionando su número de teléfono, nombre de usuario y una contraseña. Esta información debe ser almacenada de manera segura en la base de datos.

Requerimiento 2: Los usuarios deben poder crear nuevos grupos de chat, especificando un nombre para el grupo y añadiendo contactos de su lista de amigos. La información del grupo, incluyendo los miembros y la configuración, debe ser almacenada en la base de datos.

1. Read (Leer)
Requerimiento 1: Los usuarios deben poder acceder a su lista de chats, donde se muestre información como el nombre del contacto o grupo, la última vez que se recibió un mensaje y un fragmento del último mensaje. Esta información debe ser recuperada de la base de datos y presentada de manera clara y accesible.

Requerimiento 2: El sistema debe permitir a los usuarios ver el perfil de otros usuarios, mostrando información como el nombre, telefono y última conexión (o fecha de registro en sistema).

1. Update (Actualizar)
Requerimiento 1: El sistema debe permitir a los usuarios actualizar su perfil, incluyendo cambios en su nombre, telefono y estado. Cualquier cambio realizado debe ser reflejado en la base de datos y visible para sus contactos (validar...)

Requerimiento 2: TBD Los administradores deben poder actualizar la configuración de los grupos de chat, como el nombre del grupo, la imagen del grupo (TBD) y los miembros. TBD Cualquier cambio realizado debe ser registrado en un historial de cambios para mantener un registro de las modificaciones.

1. Delete (Eliminar)
Requerimiento 1: El sistema debe permitir a los usuarios eliminar mensajes de un chat, ya sea para ellos mismos o para todos los participantes del chat. Esta operación debe requerir una confirmación.

Requerimiento 2: Los usuarios deben tener la opción de eliminar su cuenta de WhatsApp. Al realizar esta acción, el sistema debe solicitar una confirmación y, una vez confirmada, eliminar todos los datos asociados a la cuenta del usuario de la base de datos, asegurando que no queden registros residuales.

Agenda:

1. Create (Crear)
Requerimiento 1: El sistema debe permitir a los usuarios crear nuevas entradas en su agenda, proporcionando información como el título del evento, la fecha y hora de inicio y fin, la ubicación y una descripción opcional. Esta información debe ser almacenada en la base de datos y asociada al perfil del usuario.

Requerimiento 2: Los usuarios deben poder agregar contactos a su agenda, incluyendo nombre, número de teléfono, dirección de correo electrónico y una nota opcional. Esta información debe ser almacenada en la base de datos y estar disponible para su consulta y uso en futuras entradas de eventos.

2. Read (Leer)
Requerimiento 1: Los usuarios deben poder acceder a una vista de su agenda, donde se muestre una lista de todos los eventos programados, organizados por fecha y hora. Esta información debe ser recuperada de la base de datos y presentada de manera clara, permitiendo a los usuarios ver detalles como el título, la fecha, la hora y la ubicación de cada evento.

Requerimiento 2: El sistema debe permitir a los usuarios consultar la información de sus contactos, mostrando detalles como nombre, número de teléfono y dirección de correo electrónico. Esta información debe ser extraída de la base de datos y presentada de manera intuitiva.

3. Update (Actualizar)
Requerimiento 1: El sistema debe permitir a los usuarios actualizar la información de sus eventos, incluyendo cambios en el título, la fecha y hora, la ubicación y la descripción. Cualquier cambio realizado debe ser reflejado en la base de datos y visible para el usuario.

Requerimiento 2: Los usuarios deben poder editar la información de sus contactos, permitiendo cambios en el nombre, número de teléfono, dirección de correo electrónico y notas. Cualquier modificación debe ser registrada en la base de datos y reflejada en la información del contacto.

4. Delete (Eliminar)
Requerimiento 1: El sistema debe permitir a los usuarios eliminar eventos de su agenda. Esta operación debe requerir una confirmación para evitar eliminaciones accidentales.

Requerimiento 2: Los usuarios deben tener la opción de eliminar contactos de su agenda. Al realizar esta acción, el sistema debe solicitar una confirmación y, una vez confirmada, eliminar todos los datos asociados al contacto de la base de datos, asegurando que no queden registros residuales.

Instagram

1. Create (Crear)
Requerimiento 1: El sistema debe permitir a los usuarios crear nuevas cuentas de Instagram proporcionando su dirección de correo electrónico, nombre de usuario, contraseña y una foto de perfil opcional. Esta información debe ser almacenada de manera segura en la base de datos.

Requerimiento 2: Los usuarios deben poder crear nuevas publicaciones en su perfil, incluyendo TEXTO con un límite 1000 caracteres (imágenes o videos NO, pero puede agregar una referencia tipo URL si gusta), Descripción y etiquetas. La información de la publicación, junto con los archivos multimedia, debe ser almacenada en la base de datos relacionada al usuario.

1. Read (Leer)
Requerimiento 1: Los usuarios deben poder acceder a su feed de publicaciones, donde se muestre una lista de las publicaciones de las cuentas que siguen, incluyendo publicaciones y su Descripción, la cantidad de "me gusta" y comentarios. Esta información debe ser recuperada de la base de datos y presentada de manera clara y atractiva.

Requerimiento 2: El sistema debe permitir a los usuarios ver su propia PUBLICACIÓN, mostrando información como su nombre de usuario, biografía y/o descripción, número de publicaciones, seguidores y seguidos. 

1. Update (Actualizar)
Requerimiento 1: El sistema debe permitir a los usuarios actualizar su perfil, incluyendo cambios en su nombre, foto de perfil (TBD), biografía y configuración de privacidad (opcional). 

Requerimiento 2: Los usuarios deben poder editar sus publicaciones existentes, permitiendo cambios la PUBLICACIÓN. Cualquier modificación debe ser registrada en la base de datos.

1. Delete (Eliminar)
Requerimiento 1: El sistema debe permitir a los usuarios eliminar sus propias publicaciones. Esta operación debe requerir una confirmación para evitar eliminaciones accidentales.

Requerimiento 2: Los usuarios deben tener la opción de eliminar su cuenta de Instagram. Al realizar esta acción, el sistema debe solicitar una confirmación y, una vez confirmada, eliminar todos los datos asociados a la cuenta del usuario de la base de datos, asegurando que no queden registros residuales.