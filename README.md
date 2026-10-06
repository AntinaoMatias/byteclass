# byteclass

Plataforma de cursos online desarrollada con Django y Django REST Framework para la asignatura de Programación Backend. El proyecto expone una API REST para gestionar el modelo de datos completo mediante operaciones CRUD.

---

## Requisitos

- Python 3
- Servidor MariaDB o MySQL
- Git

---

## Puesta en marcha

### 1. Clonar el repositorio y crear el entorno

Descarga el proyecto y entra a la carpeta:

git clone https://github.com/AntinaoMatias/byteclass.git
cd byteclass

Crea el ambiente virtual:

python -m venv ambiente

Actívalo según tu sistema:

- En Linux:
source ambiente/bin/activate

- En Linux con fish:
source ambiente/bin/activate.fish

- En Windows:
ambiente\Scripts\activate

### 2. Instalar dependencias

Con el entorno encendido, instala los paquetes del proyecto:

pip install -r requirements.txt

### 3. Variables de entorno

Crea un archivo llamado .env en la raíz del proyecto para definir la clave secreta y la conexión a la base de datos sin dejar datos privados en el código

Archivo .env adjunto en documento aparte para la entrega de la evaluación

Recuerda que este archivo debe quedarse fuera de los commits en git.

### 4. Base de datos

Antes de correr el servidor, crea la base de datos en MariaDB o MySQL con su usuario y permisos:

Archivo .sql adjunto en documento aparte para la entrega de la evaluación

### 5. Migraciones

Aplica las migraciones para generar las tablas en el motor:

python manage.py migrate

### 6. Iniciar el proyecto

Corre el servidor de desarrollo:

python manage.py runserver

Puedes ingresar desde el navegador en:

- Panel de administración: http://127.0.0.1:8000/admin/

---

## Estructura del proyecto

```text
byteclass/
├── ambiente/               # Entorno virtual
├── byteclass/              # Aplicación principal
│   ├── fixtures/           # Datos iniciales y de prueba
│   ├── migrations/         # Archivos de migración de base de datos
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── templates/          # Plantillas HTML
│   │   └── byteclass/
│   │       ├── 404.html
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py            # Registro de modelos en el panel admin
│   ├── apps.py
│   ├── models.py           # Definición de modelos de datos
│   ├── serializer.py       # Serializadores para Django REST Framework
│   ├── tests.py
│   ├── urls.py             # Enrutamiento y registro de routers de la app
│   └── views.py            # ModelViewSets y controladores
├── core/                   # Módulo de configuración principal
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Configuración del proyecto y conexión a .env
│   ├── urls.py             # Enrutador general del proyecto
│   └── wsgi.py
├── lecciones_archivos/     # Almacenamiento de archivos y recursos de lecciones
├── .env                    # Variables de entorno (ignorado en git)
├── .gitignore              # Archivos y carpetas excluidos del repositorio
├── db.sqlite3              # Base de datos local de desarrollo
├── manage.py               # Comando de gestión de Django
├── README.md               # Documentación general del proyecto
└── requirements.txt        # Dependencias y librerías instaladas
```