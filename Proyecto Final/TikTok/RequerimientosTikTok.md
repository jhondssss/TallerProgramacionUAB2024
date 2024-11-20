///////////////////////////////////////////////////
                         ENUNCIADOS

## Create

#### Enunciado 1: Creación de un Nuevo Perfil

**Descripción:** Desarrollar una función que permita a un usuario crear un nuevo perfil en la aplicación. La función debe solicitar:

- **Nombre de usuario:** El nombre de usuario que el usuario desea utilizar.
- **Correo electrónico:** La dirección de correo electrónico del usuario.
- **Contraseña:** La contraseña para el perfil.
- **Descripción (opcional):** Una breve descripción del usuario.
- **Foto de perfil (opcional):** La URL de una imagen que servirá como foto de perfil.

**Resultado:** La función debe almacenar el nuevo perfil y confirmar su creación al usuario.

---

#### Enunciado 2: Creación de un Nuevo Video

**Descripción:** Desarrollar una función que permita a un usuario subir un nuevo video. La función debe solicitar:

- **Título del video:** Un título descriptivo para el video.
- **Descripción:** Una breve descripción del contenido del video.
- **Archivo de video:** El archivo de video que se desea subir.
- **Etiquetas (opcional):** Una lista de etiquetas relacionadas con el video para facilitar su búsqueda.

**Resultado:** La función debe almacenar el nuevo video y confirmar su creación al usuario.

---

#### Enunciado 3: Creación de un Comentario

**Descripción:** Desarrollar una función que permita a un usuario comentar en un video existente. La función debe solicitar:

- **ID del video:** El identificador del video en el que se desea comentar.
- **Texto del comentario:** El contenido del comentario que se desea publicar.

**Resultado:** La función debe almacenar el nuevo comentario y confirmar su creación al usuario.

---

## Read

#### Enunciado 1: Visualización de Perfiles

**Descripción:** Desarrollar una función que permita a un usuario ver todos los perfiles en la aplicación. La función debe mostrar:

- **Lista de perfiles:** Incluir la siguiente información para cada perfil:
  - **Nombre de usuario:** El nombre de usuario del perfil.
  - **Descripción:** La descripción del usuario (si está disponible).
  - **Número de seguidores:** La cantidad de seguidores que tiene el perfil.
  - **Número de videos:** La cantidad de videos que ha subido el perfil.

**Resultado:** La función debe permitir al usuario buscar perfiles por nombre de usuario.

---

#### Enunciado 2: Visualización de Videos

**Descripción:** Desarrollar una función que permita a un usuario ver todos los videos disponibles en la aplicación. La función debe mostrar:

- **Lista de videos:** Incluir la siguiente información para cada video:
  - **Título:** El título del video.
  - **Descripción:** Una breve descripción del contenido del video.
  - **Número de likes:** La cantidad de "me gusta" que ha recibido el video.
  - **Número de comentarios:** La cantidad de comentarios en el video.

**Resultado:** La función debe permitir al usuario filtrar videos por etiquetas o por el perfil del creador.

---

#### Enunciado 3: Visualización de Comentarios

**Descripción:** Desarrollar una función que permita a un usuario ver todos los comentarios de un video específico. La función debe solicitar:

- **ID del video:** El identificador del video del que se desean ver los comentarios.

**Resultado:** La función debe mostrar:
- **Lista de comentarios:** Incluir la siguiente información para cada comentario:
  - **Nombre de usuario:** El nombre de usuario del comentarista.
  - **Texto del comentario:** El contenido del comentario.

---

## Update

#### Enunciado 1: Actualización de un Perfil

**Descripción:** Desarrollar una función que permita a un usuario actualizar la información de su perfil. La función debe solicitar:

- **ID del perfil:** El identificador del perfil que se desea actualizar.
- **Nuevo nombre de usuario (opcional):** Un nuevo nombre de usuario.
- **Nuevo correo electrónico (opcional):** Una nueva dirección de correo electrónico.
- **Nueva descripción (opcional):** Una nueva descripción para el perfil.
- **Nueva foto de perfil (opcional):** Una nueva URL para la foto de perfil.

**Resultado:** La función debe actualizar la información del perfil y confirmar los cambios al usuario.

---

#### Enunciado 2: Actualización de un Video

**Descripción:** Desarrollar una función que permita a un usuario actualizar los detalles de un video existente. La función debe solicitar:

- **ID del video:** El identificador del video que se desea actualizar.
- **Nuevo título (opcional):** Un nuevo título para el video.
- **Nueva descripción (opcional):** Una nueva descripción para el video.
- **Nuevas etiquetas (opcional):** Una nueva lista de etiquetas para el video.

**Resultado:** La función debe actualizar los detalles del video y confirmar los cambios al usuario.

---

#### Enunciado 3 : Actualización de un Comentario

**Descripción:** Desarrollar una función que permita a un usuario actualizar un comentario existente en un video. La función debe solicitar:

- **ID del comentario:** El identificador del comentario que se desea actualizar.
- **Nuevo texto del comentario:** El nuevo contenido del comentario.

**Resultado:** La función debe actualizar el comentario y confirmar los cambios al usuario.

---

## Delete

#### Enunciado 1: Eliminación de un Perfil

**Descripción:** Desarrollar una función que permita a un usuario eliminar su perfil de la aplicación. La función debe solicitar:

- **ID del perfil:** El identificador del perfil que se desea eliminar.

**Resultado:** La función debe eliminar el perfil y confirmar la eliminación al usuario, manejando el caso en que el perfil no exista.

---

#### Enunciado 2: Eliminación de un Video

**Descripción:** Desarrollar una función que permita a un usuario eliminar un video existente de su perfil. La función debe solicitar:

- **ID del video:** El identificador del video que se desea eliminar.

**Resultado:** La función debe eliminar el video y confirmar la eliminación al usuario, manejando el caso en que el video no exista.

---

#### Enunciado 3: Eliminación de un Comentario

**Descripción:** Desarrollar una función que permita a un usuario eliminar un comentario que ha realizado en un video. La función debe solicitar:

- **ID del comentario:** El identificador del comentario que se desea eliminar.

**Resultado:** La función debe eliminar el comentario y confirmar la eliminación al usuario, manejando el caso en que el comentario no exista.

---

--- Ante cualquier duda consultar con el Docente/Auxiliar. ---