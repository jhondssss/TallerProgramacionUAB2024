///////////////////////////////////////////////////
                         ENUNCIADOS

## Create


#### Enunciado 1: Creación de una Cuenta de Usuario


**Descripción:** Desarrollar una función que permita a un nuevo usuario registrarse en Facebook. La función debe solicitar:


- **Nombre completo:** El nombre y apellido del usuario.

- **Correo electrónico:** Una dirección de correo electrónico válida para la cuenta.

- **Contraseña:** Una contraseña segura que el usuario utilizará para acceder a su cuenta.

- **Fecha de nacimiento:** La fecha de nacimiento del usuario para verificar la edad.

- **Género (opcional):** Selección del género del usuario.


**Resultado:** La función debe crear una nueva cuenta de usuario y enviar un correo de verificación, mostrando un mensaje de éxito al usuario.

#### Enunciado 2: Creación de una Nueva Publicación

**Descripción:** Desarrollar una función que permita a un usuario crear una nueva publicación en su perfil. La función debe solicitar:

- **Contenido de la publicación:** El texto que el usuario desea publicar.
- **Imágenes o videos (opcional):** Archivos multimedia que el usuario desea adjuntar a la publicación.
- **Etiquetas (opcional):** Palabras clave o menciones a otros usuarios que se pueden incluir en la publicación.

**Resultado:** La función debe almacenar la nueva publicación y confirmar su creación al usuario.

---

#### Enunciado 3: Creación de un Comentario en una Publicación

**Descripción:** Desarrollar una función que permita a un usuario dejar un comentario en una publicación. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación en la que se desea comentar.
- **Contenido del comentario:** El texto del comentario que se desea dejar.

**Resultado:** La función debe almacenar el nuevo comentario y confirmar su publicación al usuario.

---

#### Enunciado 4: Creación de una Respuesta a un Comentario

**Descripción:** Desarrollar una función que permita a un usuario responder a un comentario en una publicación. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación que contiene el comentario.
- **ID del comentario:** El identificador del comentario al que se desea responder.
- **Contenido de la respuesta:** El texto de la respuesta que se desea dejar.

**Resultado:** La función debe almacenar la nueva respuesta y confirmar su publicación al usuario.

---

## Read

#### Enunciado 1: Visualización del Feed de Publicaciones

**Descripción:** Desarrollar una función que permita a un usuario ver su feed de publicaciones. La función debe mostrar:

- **Lista de publicaciones:** Incluir la siguiente información para cada publicación:
  - **Nombre del autor:** El nombre del usuario que publicó.
  - **Contenido de la publicación:** El texto de la publicación.
  - **Número de reacciones:** La cantidad de "me gusta" y otras reacciones.
  - **Comentarios:** Un resumen de los comentarios más recientes.

**Resultado:** La función debe permitir al usuario navegar por su feed de publicaciones.

---

#### Enunciado 2: Visualización de Comentarios en una Publicación

**Descripción:** Desarrollar una función que permita a un usuario ver todos los comentarios de una publicación específica. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación de la cual se desean ver los comentarios.

**Resultado:** La función debe mostrar:
- **Lista de comentarios:** Incluir la siguiente información para cada comentario:
  - **Nombre del autor:** Quien hizo el comentario.
  - **Contenido del comentario:** El texto del comentario.
  - **Número de reacciones al comentario:** La cantidad de reacciones que ha recibido el comentario.

---

#### Enunciado 3: Visualización del Perfil de un Usuario

**Descripción:** Desarrollar una función que permita a un usuario ver su propio perfil o el de otro usuario. La función debe mostrar:

- **Nombre completo:** El nombre del usuario.
- **Foto de perfil:** La imagen de perfil del usuario.
- **Lista de publicaciones:** Mostrar todas las publicaciones realizadas por el usuario.

**Resultado:** La función debe permitir al usuario ver la información de perfil seleccionada.

---

## Update

#### Enunciado 1: Actualización de una Publicación

**Descripción:** Desarrollar una función que permita a un usuario actualizar el contenido de una publicación existente. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación que se desea actualizar.
- **Nuevo contenido de la publicación:** El nuevo texto que se desea publicar.

**Resultado:** La función debe actualizar la publicación y confirmar los cambios al usuario.

---

#### Enunciado 2: Actualización de un Comentario

**Descripción:** Desarrollar una función que permita a un usuario actualizar un comentario existente en una publicación. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación donde se encuentra el comentario.
- **ID del comentario:** El identificador del comentario que se desea actualizar.
- **Nuevo contenido del comentario:** El texto actualizado del comentario.

**Resultado:** La función debe actualizar el comentario y confirmar los cambios al usuario.

---

#### Enunciado 3: Actualización de una Respuesta a un Comentario

**Descripción:** Desarrollar una función que permita a un usuario actualizar una respuesta a un comentario. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación que contiene el comentario.
- **ID del comentario:** El identificador del comentario al que se desea actualizar la respuesta.
- **ID de la respuesta:** El identificador de la respuesta que se desea actualizar.
- **Nuevo contenido de la respuesta:** El texto actualizado de la respuesta.

**Resultado:** La función debe actualizar la respuesta y confirmar los cambios al usuario.

---

## Delete

#### Enunciado 1: Eliminación de una Publicación

**Descripción:** Desarrollar una función que permita a un usuario eliminar una publicación de su perfil. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación que se desea eliminar.

**Resultado:** La función debe eliminar la publicación y confirmar la eliminación al usuario, manejando el caso en que la publicación no exista.

---

#### Enunciado 2: Eliminación de un Comentario

**Descripción:** Desarrollar una función que permita a un usuario eliminar un comentario de una publicación. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación que contiene el comentario.
- **ID del comentario:** El identificador del comentario que se desea eliminar.

**Resultado:** La función debe eliminar el comentario y confirmar la eliminación al usuario, manejando el caso en que el comentario no exista.

---

#### Enunciado 3: Eliminación de una Respuesta a un Comentario

**Descripción:** Desarrollar una función que permita a un usuario eliminar una respuesta a un comentario. La función debe solicitar:

- **ID de la publicación:** El identificador de la publicación que contiene el comentario.
- **ID del comentario:** El identificador del comentario que contiene la respuesta.
- **ID de la respuesta:** El identificador de la respuesta que se desea eliminar.

**Resultado:** La función debe eliminar la respuesta y confirmar la eliminación al usuario, manejando el caso en que la respuesta no exista.