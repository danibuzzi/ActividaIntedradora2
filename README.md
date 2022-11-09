
Trabajo Final Proyecto Integrador de Programación 

INTEGRANTES GRUPO DE TRABAJO Nº 15:

Buzzi, Daniel Alejandro  -- daniel.buzzi@gmail.com
Torres, Brenda           --  torresbrenda333@gmail.com



En esta actividad integradora hemos volcado los conocimientos adquiridos durante el cursado del módulo de programador (programacion, bases de datos y proyecto integrador) y los  aprendizajes resultantes de nuestra investigación.

El trabajo presentado consiste en una aplicación web para una disqueria.


Tecnologías y lenguajes empleados:

- Python (como lenguaje de programación base)
- Bases de datos MySql Server (para el almacenamiento y la gestión de los datos)
- Libreria Flask (es un framework que permite la elaboración de un sitio web utilizando lenguaje python)
- Lenguaje HTML (para el maquetado del esquema de las vistas del sitio).
- Hojas de estilo en cascada (CSS) (para dar formato y estilo a las paginas del sitio)
- Framework Bootstrap (además de proveer de las herramientas necesarias para dar formato y estilo a las páginas del sitio, facilita la implemetación del diseño responsivo).
- Lenguaje javascript (para la implementación de rutinas del lado del cliente).


Requerimientos de funcionamiento del programa:

Una vez descargado el codigo fuente, para el uso del programa se requiere instalar previamente las siguientes librerias:

- Framework Flask --- pip install flask
- Conector a MySql Server para python --- pip install mysql-connector-python

Por simplicidad se recomienda, para la prueba local del sistema, instalar y ejecutar la aplicacion XAMPP .Procedemos a iniciar  el servidor web Apache y el servidor de base de datos MySql Server y ejecutamos el administrador o gestor para la base de datos (phpmyadmin que ya incorpora XAMP) ,y mediante el uso del script disqueria_script_valido.sql generamos la base de datos.

Una vez cumplido estos requerimientos anteriores se ejecuta el programa con el comando: --  python app.py.  
Para visualizar la aplicacion web es preciso abrir el software navegador de internet y dirigirse a la direccion  http://localhost:5000/


En la codificación del sitio se ha seguido el paradigma de programación  orientado a objetos (P.O.O.) ,y se ha organizado el código de la aplicacion mediante el uso del patrón de diseño MVC (modelo- vista- controlador) que permite las dividir tareas en capas , cada de ellas una con responsabilidad específica}.Este enfoque promueve una mejor organización del programa, facilitando la detección y depuración de errores y las tareas de mantenimiento , incluidas la mejora del código y el agregado de nuevas funcionalidades.


La aplicación para la disqueria Formosa proporciona las siguientes funcionalidades:

- Muestra de los datos principales de los 3 albumes con fecha de lanzamiento más reciente.
- Gestion de los álbumes (alta , modificación y eliminación de datos del álbum)
- Listado de álbumes ordenados por id de album.
- Listado de álbumes ordenados por intérprete.
- Listado de álbumes ordenados por género musical.
- Búsqueda de álbum por nombre del álbum.






