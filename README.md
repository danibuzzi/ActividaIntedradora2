
Trabajo Final Proyecto Integrador de Programación 

INTEGRANTES GRUPO DE TRABAJO Nº 15:

Buzzi, Daniel Alejandro  -- daniel.buzzi@gmail.com
Torres, Brenda           --  torresbrenda333@gmail.com



En esta actividad integradora hemos volcado los conocimientos adquiridos durante el cursado del módulo de programación, integrando el  lenguaje python y la gestión de bases de datos y aprendizajes resultantes de nuestra investigación.
El trabajo presentado consiste en una aplicación web para una disqueria.

La aplicación para la disqueria Formosa proporciona las siguientes funcionalidades:

- Muestra de los datos principales de los 3 albumes con  fecha de lanzamiento más reciente.
- Gestion de los álbumes (alta , modificación y eliminación de datos del álbum)
- Listado de álbumes cargados sin ordenamiento.
- Listado de álbumes ordenados por intérprete.
- Listado de álbumes ordenados por género musical.
- Búsqueda de álbum por nombre del álbum.

Tecnologías empleadas:

- Python (como lenguaje de programación base)
- Bases de datos MySql Server (para el almacenamiento y la gestión de los datos)
- Libreria Flask (es un framework que permite la elaboración de un sitio web utilizando lenguaje python)
- Lenguaje HTML (para el maquetado del esquema de las vistas del sitio).
- Hojas de estilo en cascada (CSS) (para dar formato y estilo a las paginas del sitio)
- Framework Bootstrap (además de proveer de las herramientas necesarias para dar formato y estilo a las páginas del sitio, facilita la implemetación del diseño responsivo).
- Lenguaje javascript (para la implementación de rutinas del lado del cliente).


Requerimientos de funcionamiento del programa:

Para el uso del programa se requiere instalar previamente las siguientes librerias:

- Framework Flask --- pip install Flask
- Conector a MySql Server para python --- pip install mysql-connector-python

 Para cargar la base de datos se debe generar con el script disqueria_script_valido.sql. Por simplicidad se recomienda para la prueba local del sistema, instalar y ejecutar la aplicacion XAMPP , levantando  el servidor web Apache y el servidor de base de datos MySql Server y ejecutar el administrador para la base de datos (phpmyadmin por ejemplo) ,y luego generar la base de datos.

Una vez cumplido estos requerimientos se ejecuta el programa con el comando: --  python app.py  
Se carga  en el software navegador de internet el sitio escribiendo la dirección http://localhost:5000/.


En cuanto a la programacion del sitio se ha seguido el paradigma de programación  orientado a objetos (P.O.O.) ,y se ha organizado la aplicacion mediante el uso del patrón de diseño MVC (modelo- vista- controlador) que permite dividir el código en capas , cada de ellas una con responsabilidad específica}.Este enfoque promueve una mejor organización del código, facilitando la detección y depuración de errores y las tareas de mantenimiento , incluidas la mejora del código y el agregado de nuevas funcionalidades.









