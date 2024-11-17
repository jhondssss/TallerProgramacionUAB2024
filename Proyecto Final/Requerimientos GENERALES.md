////////////////////////////////////////////////////
Objetivo del Proyecto:

Desarrollar una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) que simule la gestión de un producto del mundo real. Esta aplicación debe permitir a los usuarios interactuar con los datos del producto de manera eficiente y efectiva, implementando las mejores prácticas de desarrollo de software, principios de programación orientada a objetos (OOP), y estructuras de datos adecuadas.

Requisitos Técnicos:

Estructura de Datos: Utilizar estructuras de datos adecuadas (listas, diccionarios, conjuntos, etc.) para almacenar y gestionar la información de manera eficiente.

Programación Orientada a Objetos (OOP): Implementar clases y objetos para representar los productos y sus atributos, así como las operaciones CRUD. Se deben aplicar conceptos como herencia, encapsulamiento y polimorfismo donde sea relevante.

Operaciones CRUD:

Crear: Permitir a los usuarios agregar nuevos productos o registros.
Leer: Facilitar la visualización de los productos existentes, con opciones de filtrado y búsqueda.
Actualizar: Permitir la modificación de la información de los productos ya registrados.
Eliminar: Proporcionar la opción de eliminar productos del sistema.
Buenas Prácticas de Desarrollo: Seguir principios de diseño de software, como la separación de responsabilidades, la claridad en la nomenclatura de variables y funciones, y la documentación adecuada del código.

Lógica de Programación: Implementar una lógica clara y eficiente para manejar las interacciones del usuario y el flujo de datos en la aplicación.

Entrega del Proyecto:

El proyecto se desarrollará en equipos, y cada equipo deberá presentar su aplicación CRUD al final del periodo de desarrollo. La presentación incluirá una demostración de la funcionalidad de la aplicación, así como una explicación de las decisiones de diseño tomadas y cómo se han aplicado los conceptos aprendidos en el Taller de Programación.

Evaluación:

La evaluación se basará en la funcionalidad de la aplicación, la calidad del código, la implementación de OOP y estructuras de datos, el cumplimiento de las buenas prácticas de desarrollo y la presentación del proyecto. Se valorará la lógica de programación, legibilidad, funcionalidad y la efectividad de la solución propuesta, NO se valorará la interfaz gráfica ya que la idea del proyecto no es que se vea "bonito", sino que cumpla con la FUNCIONALIDAD definida por los ENUNCIADOS.
///////////////////////////////////////////////////

////////////////////////////////////////////////////
--- Ante cualquier duda consultar con el Docente/Auxiliar. ---
///////////////////////////////////////////////////

Requisitos para el Desarrollo del Sistema:

1 Su sistema debe implementar las cuatro operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar). Se valorarán especialmente los proyectos que incluyan al menos dos de los tres enunciados desarrollados, junto con sus funcionalidades correspondientes para cada operación. Sin embargo, si su proyecto cuenta con al menos una funcionalidad (enunciado) para cada operación del CRUD, se considerará como mínimamente desarrollado y suficiente para su defensa.

Al seleccionar los enunciados con su equipo, es crucial que lo hagan de manera cuidadosa, ya que algunos enunciados pueden depender de otros para funcionar correctamente.

Nota Importante: Los enunciados están relacionados con el producto real que les ha sido asignado. Al evaluar su proyecto, se tendrá en cuenta que cada enunciado cumpla con su título. Por ejemplo, si el enunciado indica "Listar publicaciones", su sistema debe listar publicaciones y no realizar ni mostrar otras funcionalidades que no se alineen con el contexto lógico de lo solicitado.

2 El desarrollo de su sistema debe ser realizado por todos los miembros del equipo. Para garantizar una colaboración efectiva, cada integrante debe enviar sus contribuciones de manera individual cada vez que complete una funcionalidad.

Por ejemplo, al finalizar la implementación de una funcionalidad específica, como el registro de información (operación CREATE), cada miembro debe subir su código al repositorio del proyecto en la carpeta designada para su equipo. Cada equipo cuenta con un directorio único que lleva el nombre del producto asignado, donde deberán realizar sus envíos utilizando el método de FORK y Pull Request (PR).

En caso de que un miembro del equipo no pueda realizar el proceso de envío individual, es fundamental que el equipo tenga un repositorio compartido donde los cuatro miembros puedan integrar su código. Esto permitirá que el docente o auxiliar pueda visualizar los cambios realizados en el proyecto a medida que avancen en su desarrollo.

Es importante seguir estas directrices para asegurar una buena organización y facilitar la revisión del progreso del proyecto.

3 La aplicación DEBE mostrar el contenido de publicaciones, fotos, videos, etc., en orden descendente. Esto significa que los elementos más recientemente registrados en el sistema deben aparecer primero. Por ejemplo, si la base de datos contiene 1000 registros, se deben mostrar los últimos registros en la parte superior de la lista.

Para las operaciones que impliquen una lectura (READ), como listar elementos, se debe garantizar que el último registro (o el más recientemente actualizado >> UPDATE) se muestre en la parte superior, seguido por los registros anteriores en orden cronológico.

A continuación, se presentan ejemplos específicos:

Lista de Usuarios: Al listar los usuarios, el último usuario registrado debe aparecer en la parte superior de la lista, seguido por el penúltimo usuario registrado, y así sucesivamente. Además, se debe incluir la fecha de registro de cada usuario para proporcionar contexto temporal.

Lista de Publicaciones: Al mostrar las publicaciones, las más recientes deben aparecer primero, comenzando con la última publicación realizada en la parte superior, seguida de la penúltima publicación, y así sucesivamente.

EJEMPLO:

Publicación A: "¡Hoy fue un gran día! Disfruté de una caminata en el parque."
Fecha: 15 de octubre de 2023, 18:30
Usuario: JuanaMorales123

Publicación D: "Acabo de terminar un libro increíble. ¡Lo recomiendo a todos!"
Fecha: 14 de octubre de 2023, 14:15
Usuario: ...

Publicación I: "Preparando una cena especial para esta noche."
Fecha: 13 de octubre de 2023, 20:00
Usuario: ...

Publicación M: "Hoy celebramos el cumpleaños de mi mejor amigo. ¡Fue una fiesta inolvidable!"
Fecha: 12 de octubre de 2023, 22:45
Usuario: JohnBonachon5345...

Publicación O: "Asistí a un taller de fotografía. Aprendí mucho sobre composición."
Fecha: 11 de octubre de 2023, 10:30

Publicación E: "Ayer vi una película que me hizo reflexionar. ¡Qué gran actuación!"
Fecha: 10 de octubre de 2023, 21:00

Publicación W: "Empezando una nueva serie en Netflix. ¡No puedo esperar para ver más!"
Fecha: 9 de octubre de 2023, 19:15

Publicación T: "Hoy hice una limpieza profunda en casa. ¡Me siento renovado!"
Fecha: 8 de octubre de 2023, 16:00

Publicación I: "Recibí una buena noticia en el trabajo. ¡Vamos por más!"
Fecha: 7 de octubre de 2023, 11:45

Publicación P: "Pasé un rato agradable con la familia. Siempre es bueno estar juntos."
Fecha: 6 de octubre de 2023, 13:30

Este enfoque asegura que los usuarios puedan acceder fácilmente a la información más reciente y relevante en el sistema.

4 Su sistema DEBE tener un Menú que simule la interfaz gráfica que tendría el producto real (JAMÁS SE HA PEDIDO INTERFACES GRÁFICAS como Sitios WEB o similares, si el equipo decidió o decide realizarlo queda bajo su propia responsabilidad, lo mínimo esperado es un menú visible para el usuario por CONSOLA), por ejemplo:

Menú Twitter:

Seleccione la opción a realizar:
1. Registrar usuario
2. Iniciar Sesión con usuario ya registrado

(Si selecciona 1 lo esperado sería un nuevo menú como el siguiente)
Menú Registrar usuario:
1. Ingresar datos del usuario
2. Volver al menú anterior
3. etc.

(Si selecciona la opción 2)
Menú Iniciar Sesión con usuario ya registrado:
1. Ingresar datos de inicio de sesión (Si escoge esta opción mostrar en pantalla solicitud para pedir Username y Password por ejemplo)
   Escriba su nombre de Usuario: .... 
   Escriba su contraseña
2. Volver al menú anterior

(En el caso de haberse identificado como un usuario en el sistema:)
Menú Twitter:
1. Publicar Tweet (ejemplo de un CREATE/CREAR)
2. Ver mis tweets (ejemplo de un READ/LEER)
3. Ver tweets de otros usuarios (ejemplo de un READ/LEER)
4. Modificar/Editar Tweet (ejemplo de un UPDATE/ACTUALIZAR)
5. Eliminar Tweet (ejemplo de un DELETE/BORRAR)
6. Eliminar mi cuenta para siempre (ejemplo de un DELETE/BORRAR)
7. Volver al menú anterior
8. etc.
9. Salir del sistema
    
VER IMÁGENES DE REFERENCIA (Cómo lo vería un Usuario Final)

Uso de Menú por CONSOLA:
![Menú 1](../Proyecto%20Final/MenuParte1.png)
************************
![Menú 2](../Proyecto%20Final/MenuParte2.png)
************************
![Menú 3](../Proyecto%20Final/MenuParte3.png)
************************
![Menú 4](../Proyecto%20Final/MenuParte4Final.png)

///////////////////////////////////////////////////
Nota Importante sobre Identificadores:

El ID mencionado en los enunciados no tiene que ser necesariamente un identificador numérico. Pueden utilizar cualquier tipo de identificador que su producto asigne a los usuarios, como nombres de usuario, números de teléfono, o cualquier otro formato que se considere adecuado.

Por ejemplo, en Facebook se utilizan dos tipos de identificadores: uno numérico y otro de cadena. El identificador numérico es un valor asignado en la base de datos, como 100005103218972, mientras que el identificador de cadena puede ser un nombre de usuario, como "IngNaranja". Ambos identificadores permiten acceder al mismo perfil a través de las URLs: https://www.facebook.com/IngNaranja/ y https://www.facebook.com/100005103218972.

Esta aclaración es especialmente relevante para las operaciones de búsqueda, listado, y las funciones de Read, Update y Delete. Por lo tanto, es recomendable considerar cualquier tipo de identificador mencionado anteriormente. Eviten utilizar ejemplos de URLs largas que incluyan "HTTPS://...", ya que esto es únicamente ilustrativo.

///////////////////////////////////////////////////
Nota importante sobre la Coherencia en el Formato de Fechas y Horas para Productos de Software:

Para todos los productos de software, se espera que haya coherencia entre la interfaz y la representación de fechas y horas que se muestran a los usuarios.

Por ejemplo, en Facebook, se debe mostrar la fecha y hora exactas de una publicación o comentario. Sin embargo, si han transcurrido más de 24 horas desde su registro, solo se debe mostrar la fecha (sin la hora) para la publicación o comentario.

En el caso de Netflix, aunque no se proporciona la fecha y hora de creación de las películas o series, se indica el "Año" en el que fueron lanzadas, lo que permite a los usuarios conocer el periodo de estreno.

Para YouTube, la fecha se presenta de la siguiente manera: Fecha de Estreno: 17 Oct 2024

Es fundamental seguir estos lineamientos para asegurar una experiencia de usuario consistente y clara en la visualización de información temporal.
///////////////////////////////////////////////////
Consideraciones para Productos de Software que Utilizan Multimedia:

Para todos los productos de software, especialmente aquellos que manejan imágenes (como Facebook, Pinterest, Instagram), videos (como Netflix y YouTube) y música (como Spotify), el sistema a desarrollar no incluirá una interfaz gráfica. Sin embargo, se permitirá la representación de fotos, canciones y videos a través de URLs. Esto significa que se podrá simular una publicación que incluya una imagen, canción o video mediante un campo que contenga la ruta o dirección URL correspondiente a un recurso multimedia real.

Ejemplo: 
(CREATE) Creación de una Nueva Publicación
Desarrollar una función que permita a un usuario crear una nueva publicación en su perfil. Esta función debe solicitar la siguiente información:

Imagen o Video: La URL de la imagen o video que se desea publicar. Por ejemplo:

Para una imagen: https://i.sstatic.net/l60Hf.png
Para un video: https://www.youtube.com/watch?v=J327tGiQ2Uc&ab_channel=CONPAZCOMPUESTO
Descripción: Un texto que describa la publicación.

Hashtags: Una lista de hashtags que se deseen agregar a la publicación.

La función debe almacenar la nueva publicación y confirmar su creación al usuario.

(READ) Visualización de Publicaciones de un Perfil
Posteriormente, al utilizar la funcionalidad para mostrar o listar las publicaciones de un perfil (operación Read de un CRUD), se deberá incluir el mismo URL registrado. De esta manera, para la imagen o video de la publicación, se mostrará el mismo URL en la pantalla, permitiendo a los usuarios acceder al contenido multimedia correspondiente.










