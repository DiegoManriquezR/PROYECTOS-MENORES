# Proyectos menores

Repositorio con varios proyectos de práctica desarrollados principalmente con Python, HTML, CSS, JavaScript, Bootstrap, Django y MySQL. Incluye ejercicios de consola, CRUDs, sitios web estáticos y una aplicación web de reservas.

## Estructura general

| Carpeta | Tipo de proyecto | Tecnologías principales |
| --- | --- | --- |
| `ALGORITMOS PHYTON` | Ejercicios y programas de práctica en Python | Python, Tkinter, MySQL, Requests, bcrypt, Turtle |
| `CRUD DE ALUMNOS` | CRUDs de consola/escritorio y conexión a base de datos | Python, Tkinter, MySQL, Requests |
| `CRUD JS` | CRUD web de productos | HTML, JavaScript, Bootstrap |
| `BIBLIOTECA` | Sitio web de biblioteca con catálogo CRUD | HTML, CSS, JavaScript, Bootstrap, localStorage |
| `PAGINA DE EVENTOS` | Sitio web de eventos y reservas | HTML, CSS, JavaScript, Bootstrap, localStorage |
| `PRIMERA PAGINA` | Primeros sitios web de práctica | HTML, CSS, JavaScript, Bootstrap |
| `RESERVAS` | Sistema web de reservas de salas | Python, Django, Bootstrap, SQLite/MySQL |
| `VENTAS1` | Sitio web de ventas | HTML, CSS, JavaScript |

## ALGORITMOS PHYTON

Colección de ejercicios sueltos de Python usados para practicar lógica de programación, estructuras de datos, funciones, ciclos, condicionales, clases y conexión con bases de datos.

Tecnologías usadas:

- Python.
- Tkinter para interfaces gráficas simples.
- MySQL mediante `mysql.connector`.
- Requests para consumo de APIs.
- bcrypt para manejo de contraseñas.
- Turtle para ejercicios gráficos.
- PyMongo en ejercicios de conexión a MongoDB.

Programas y funciones destacadas:

- Calculadoras y validaciones: cálculo de IMC, promedios, facturas, ventas, tablas de multiplicar y validación de datos.
- Ejercicios de listas, tuplas y cadenas: manejo de colecciones, búsqueda, ordenamiento y recorridos.
- Programación orientada a objetos: clases, herencia, herencia múltiple, polimorfismo, encapsulamiento, getters y setters.
- Ejercicios gráficos: uso de `turtle` para dibujar o animar elementos.
- Consumo de APIs: archivo `api.py`, que obtiene chistes desde JokeAPI.
- Sistema con login e indicadores: archivos `menu.py`, `funciones.py` y `bd/conexion.py`, que trabajan con usuarios, contraseñas e indicadores almacenados en MySQL.

Cómo ejecutar:

```bash
python "ALGORITMOS PHYTON/nombre_del_archivo.py"
```

Nota: varios archivos son ejercicios independientes de práctica, por lo que algunos requieren datos por consola o una base de datos configurada.

## CRUD DE ALUMNOS

Proyecto con distintas versiones de CRUD usando Python. Aunque la carpeta se llama `CRUD DE ALUMNOS`, también incluye ejemplos para productos, usuarios, categorías, proveedores, transacciones y personas.

Tecnologías usadas:

- Python.
- Tkinter para interfaz de escritorio.
- MySQL con `mysql.connector`.
- Requests para consumo de APIs externas.

Programas principales:

- `estudiantes.py`: CRUD simple en consola para crear, leer, actualizar y eliminar estudiantes guardados en una lista.
- `inicio.py`: aplicación Tkinter para gestionar productos con operaciones de insertar, mostrar, actualizar y eliminar.
- `funciones.py`: funciones CRUD para productos usando MySQL.
- `bd/conexion.py`: conexión a MySQL usando host local, usuario `root`, base de datos `base_datos` y puerto `3307`.
- `menu.py`: interfaz Tkinter con inicio de sesión, registro de usuario y consulta de indicadores.
- `menu1.py`, `funciones1.py` y `bd/conexiones1.py`: CRUD más amplio para usuarios, productos, categorías, proveedores y transacciones.
- `api.py`: ejemplo de consumo de API para obtener un chiste desde JokeAPI.

Funciones principales:

- Registrar datos.
- Listar registros.
- Editar registros existentes.
- Eliminar registros.
- Conectar con MySQL.
- Consultar información externa mediante API.

Cómo ejecutar:

```bash
python "CRUD DE ALUMNOS/estudiantes.py"
python "CRUD DE ALUMNOS/inicio.py"
```

Para los archivos con MySQL, se debe tener creada la base de datos correspondiente y ajustar la conexión si el puerto, usuario o contraseña son distintos.

## CRUD JS

Aplicación web simple para administrar productos desde una tabla usando JavaScript y Bootstrap.

Tecnologías usadas:

- HTML.
- JavaScript.
- Bootstrap 5.

Qué hace:

- Muestra una tabla de productos.
- Abre un modal para ingresar datos.
- Permite agregar productos con nombre, precio, categoría y descripción.
- Incluye validaciones básicas del formulario.
- Tiene botones preparados para editar y eliminar productos.

Archivo principal:

- `CRUD JS/index.html`
- `CRUD JS/funciones.js`

Cómo ejecutar:

Abrir el archivo `CRUD JS/index.html` en el navegador.

## BIBLIOTECA

Sitio web llamado "Librería de Hogwarts", con página de inicio, catálogo de libros y formulario de contacto.

Tecnologías usadas:

- HTML.
- CSS.
- JavaScript.
- Bootstrap 5.
- Bootstrap Icons.
- localStorage del navegador.

Qué hace:

- Presenta una página de bienvenida.
- Administra un catálogo de libros.
- Permite agregar, editar y eliminar libros.
- Filtra libros por género.
- Busca libros por título o autor.
- Guarda los libros en `localStorage`.
- Valida formulario de contacto.
- Guarda mensajes de contacto en `localStorage`.

Archivos principales:

- `BIBLIOTECA/index.html`
- `BIBLIOTECA/catalogolibros.html`
- `BIBLIOTECA/contacto.html`
- `BIBLIOTECA/funcionescrud.js`
- `BIBLIOTECA/estilos.css`

Cómo ejecutar:

Abrir `BIBLIOTECA/index.html` en el navegador.

## PAGINA DE EVENTOS

Sitio web temático de eventos llamado "El Palacio de Baile de Disco Stu". Incluye páginas de inicio, eventos, galería, blog, contacto y autenticación.

Tecnologías usadas:

- HTML.
- CSS.
- JavaScript.
- Bootstrap 5.
- Bootstrap Icons.
- localStorage.
- Archivos multimedia: imágenes, GIF, audio MP3 y video MP4.

Qué hace:

- Muestra información de eventos.
- Tiene cuenta regresiva para eventos.
- Permite reservas desde formularios.
- Guarda reservas en `localStorage`.
- Incluye galería filtrable por categoría.
- Permite ampliar imágenes en modal.
- Tiene blog con comentarios y sistema de votos.
- Incluye registro, login y cierre de sesión usando `localStorage`.
- Maneja música de fondo y botón de silencio.

Archivos principales:

- `PAGINA DE EVENTOS/index.html`
- `PAGINA DE EVENTOS/eventos.html`
- `PAGINA DE EVENTOS/galeria.html`
- `PAGINA DE EVENTOS/blog.html`
- `PAGINA DE EVENTOS/contacto.html`
- `PAGINA DE EVENTOS/autenticacionusuarios.html`
- `PAGINA DE EVENTOS/funciones.js`
- `PAGINA DE EVENTOS/estilos.css`

Cómo ejecutar:

Abrir `PAGINA DE EVENTOS/index.html` en el navegador.

## PRIMERA PAGINA

Proyecto de práctica inicial con páginas HTML, estilos CSS y algunos ejercicios con Bootstrap.

Tecnologías usadas:

- HTML.
- CSS.
- JavaScript.
- Bootstrap.

Qué hace:

- Presenta páginas básicas de navegación.
- Incluye páginas de contacto y nosotros.
- Contiene una subcarpeta `MI PRIMERA PAGINA` con pruebas de Bootstrap, navbar, tarjetas, modales y scripts.

Archivos principales:

- `PRIMERA PAGINA/index.html`
- `PRIMERA PAGINA/paginas/contacto.html`
- `PRIMERA PAGINA/paginas/nosotros.html`
- `PRIMERA PAGINA/MI PRIMERA PAGINA/index.html`
- `PRIMERA PAGINA/MI PRIMERA PAGINA/funciones.html`

Cómo ejecutar:

Abrir `PRIMERA PAGINA/index.html` o `PRIMERA PAGINA/MI PRIMERA PAGINA/index.html` en el navegador.

## RESERVAS

Aplicación web completa en Django para gestionar reservas de salas.

Tecnologías usadas:

- Python.
- Django.
- Bootstrap 5.
- CSS personalizado.
- SQLite o MySQL.
- `mysqlclient` si se usa MySQL.

Qué hace:

- Página de inicio del sistema.
- CRUD de salas.
- CRUD de reservas.
- Filtros de búsqueda para salas por texto y capacidad.
- Filtros de reservas por sala, fecha y periodo.
- Validaciones de formularios.
- Evita reservas con horarios solapados.
- Impide eliminar salas con reservas asociadas.
- Valida horarios permitidos: lunes a viernes, entre 08:00 y 20:00.
- Valida duración mínima de 15 minutos, máxima de 480 minutos y múltiplos de 15.

Modelos principales:

- `Sala`: nombre, capacidad, equipo y ubicación.
- `Reserva`: usuario, sala, fecha/hora y duración.

Archivos principales:

- `RESERVAS/manage.py`
- `RESERVAS/requirements.txt`
- `RESERVAS/gestor_reservas/settings.py`
- `RESERVAS/reservas/models.py`
- `RESERVAS/reservas/forms.py`
- `RESERVAS/reservas/views.py`
- `RESERVAS/reservas/templates/`

Cómo ejecutar:

```bash
cd RESERVAS
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Luego abrir:

```text
http://127.0.0.1:8000/
```

## VENTAS1

Sitio web de ventas llamado "Bebé Feliz", orientado a mostrar productos y una página de contacto.

Tecnologías usadas:

- HTML.
- CSS.
- JavaScript.

Qué hace:

- Presenta una página principal de tienda.
- Muestra productos en páginas internas.
- Incluye página de contacto.
- Usa hojas de estilo separadas para inicio, productos y contacto.

Archivos principales:

- `VENTAS1/index.html`
- `VENTAS1/paginas/productos.html`
- `VENTAS1/paginas/contacto.html`
- `VENTAS1/estilos.css`
- `VENTAS1/paginas/estilosproductos.css`
- `VENTAS1/paginas/estiloscontacto.css`

Cómo ejecutar:

Abrir `VENTAS1/index.html` en el navegador.

## Requisitos generales

Para los proyectos web estáticos:

- Navegador web moderno.
- Conexión a internet si se cargan librerías desde CDN, como Bootstrap.

Para los proyectos Python:

- Python 3.
- Instalar dependencias según el archivo o proyecto.
- MySQL si el programa usa base de datos.

Dependencias frecuentes:

```bash
pip install mysql-connector-python requests bcrypt pymongo
```

Para Django:

```bash
pip install -r RESERVAS/requirements.txt
```

## Notas

- Algunos archivos son ejercicios de aprendizaje y pueden requerir ajustes antes de ejecutarse.
- Los proyectos web con `localStorage` guardan datos solo en el navegador donde se usan.
- Los proyectos con MySQL requieren que la base de datos, tablas, usuario, contraseña y puerto coincidan con la configuración del código.
