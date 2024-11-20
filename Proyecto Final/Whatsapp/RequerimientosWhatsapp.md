///////////////////////////////////////////////////
                         ENUNCIADOS

## Create

#### Enunciado 1: Creación de un Nuevo Chat

**Descripción:** Desarrollar una función que permita al usuario crear un nuevo chat. La función debe solicitar:

- **Nombre del chat:** Un título que describa el chat (puede ser un grupo o un contacto).
- **Lista de participantes:** Los nombres o IDs de los usuarios que participarán en el chat.
- **Tipo de chat:** Indicar si es un chat individual o un grupo.

**Resultado:** La función debe almacenar el nuevo chat y confirmar su creación al usuario.

---

#### Enunciado 2: Envío de un Mensaje

**Descripción:** Desarrollar una función que permita al usuario enviar un mensaje a un chat existente. La función debe solicitar:

- **ID del chat:** El identificador del chat al que se desea enviar el mensaje.
- **Contenido del mensaje:** El texto del mensaje que se desea enviar.
- **Nombre del usuario:** Indicar quién está enviando el mensaje.

**Resultado:** La función debe almacenar el nuevo mensaje en el chat correspondiente y confirmar su envío al usuario.

---

#### Enunciado 3: Creación de un Nuevo Contacto

**Descripción:** Desarrollar una función que permita al usuario agregar un nuevo contacto a su lista. La función debe solicitar:

- **Nombre del contacto:** El nombre del nuevo contacto.
- **Número de teléfono:** El número de teléfono del contacto.
- **Foto de perfil (opcional):** Un URL que represente la foto de perfil del contacto.

**Resultado:** La función debe almacenar el nuevo contacto y confirmar su creación al usuario.

---

## Read

#### Enunciado 1: Visualización de Chats Actuales

**Descripción:** Desarrollar una función que permita al usuario visualizar todos los chats actuales. La función debe mostrar:

- **Lista de chats:** Mostrar todos los chats asociados al usuario, incluyendo:
  - **ID del chat:** Un identificador único para cada chat.
  - **Nombre del chat:** El título que describe el chat.
  - **Último mensaje:** Mostrar el contenido del último mensaje enviado en el chat.
  - **Fecha y hora del último mensaje:** Indicar cuándo se envió el último mensaje.

**Resultado:** La función debe permitir al usuario navegar entre sus chats y seleccionar uno para ver más detalles.

---

#### Enunciado 2: Visualización de Mensajes en un Chat

**Descripción:** Desarrollar una función que permita al usuario ver todos los mensajes en un chat específico. La función debe solicitar:

- **ID del chat:** El identificador del chat del que se desean ver los mensajes.

**Resultado:** La función debe mostrar:
- **Lista de mensajes:** Mostrar todos los mensajes en el chat, incluyendo:
  - **Nombre del remitente:** Indicar quién envió cada mensaje.
  - **Contenido del mensaje:** El texto del mensaje.
  - **Fecha y hora del mensaje:** Mostrar cuándo se envió el mensaje.

**Nota:** La función debe manejar el caso en que no existan mensajes en el chat.

---

#### Enunciado 3: Visualización de Contactos

**Descripción:** Desarrollar una función que permita al usuario ver todos sus contactos. La función debe mostrar:

- **Lista de contactos:** Mostrar todos los contactos almacenados, incluyendo:
  - **Nombre del contacto:** El nombre del contacto.
  - **Número de teléfono:** El número de teléfono del contacto.
  - **Foto de perfil (opcional):** Un URL que represente la foto de perfil del contacto.

**Resultado:** La función debe permitir al usuario buscar un contacto específico y manejar el caso en que no existan contactos.

---

## Update

#### Enunciado 1: Actualización de un Chat

**Descripción:** Desarrollar una función que permita al usuario actualizar la información de un chat existente. La función debe solicitar:

- **ID del chat:** El identificador del chat que se desea actualizar.
- **Nuevo nombre del chat (opcional):** Un nuevo título para el chat.
- **Nueva lista de participantes (opcional):** Actualizar los nombres o IDs de los usuarios que participarán en el chat.

**Resultado:** La función debe actualizar la información del chat y confirmar los cambios al usuario.

---

#### Enunciado 2: Actualización de un Mensaje

**Descripción:** Desarrollar una función que permita al usuario actualizar un mensaje enviado en un chat específico. La función debe solicitar:

- **ID del chat:** El identificador del chat donde se encuentra el mensaje.
- **ID del mensaje:** El identificador del mensaje que se desea actualizar.
- **Nuevo contenido del mensaje:** El texto actualizado del mensaje.

**Resultado:** La función debe actualizar el mensaje y confirmar los cambios al usuario.

---

#### Enunciado 3: Actualización de un Contacto

**Descripción:** Desarrollar una función que permita al usuario actualizar la información de un contacto existente. La función debe solicitar:

- **ID del contacto:** El identificador del contacto que se desea actualizar.
- **Nuevo nombre del contacto (opcional):** Un nuevo nombre para el contacto.
- **Nuevo número de teléfono (opcional):** Un nuevo número de teléfono para el contacto.
- **Nueva foto de perfil (opcional):** Un URL que represente la nueva foto de perfil del contacto.

**Resultado:** La función debe actualizar la información del contacto y confirmar los cambios al usuario.

---

## Delete

#### Enunciado 1: Eliminación de un Chat

**Descripción:** Desarrollar una función que permita al usuario eliminar un chat existente. La función debe solicitar:

- **ID del chat:** El identificador del chat que se desea eliminar.

**Resultado:** La función debe eliminar el chat y confirmar la eliminación al usuario, manejando el caso en que el chat no exista.

---

#### Enunciado 2: Eliminación de un Mensaje

**Descripción:** Desarrollar una función que permita al usuario eliminar un mensaje enviado en un chat. La función debe solicitar:

- **ID del chat:** El identificador del chat donde se encuentra el mensaje.
- **ID del mensaje:** El identificador del mensaje que se desea eliminar.

**Resultado:** La función debe eliminar el mensaje y confirmar la eliminación al usuario, manejando el caso en que el mensaje no exista.

---

#### Enunciado 3: Eliminación de un Contacto

**Descripción:** Desarrollar una función que permita al usuario eliminar un contacto de su lista. La función debe solicitar:

- **ID del contacto:** El identificador del contacto que se desea eliminar.

**Resultado:** La función debe eliminar el contacto y confirmar la eliminación al usuario, manejando el caso en que el contacto no exista.

---

--- Ante cualquier duda consultar con el Docente/Auxiliar. ---