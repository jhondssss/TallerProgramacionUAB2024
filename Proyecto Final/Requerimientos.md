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