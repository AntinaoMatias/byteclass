# byteclass
Repositorio para el desarrollo de plataforma de cursos online como proyecto para la materia programación backend

Este archivo readme contiene las instrucciones para la creación de este proyecto sin omitir ni un solo paso.

## Creación del ambiente virtual

* Abrimos la terminal de vscode y ejecutamos el siguiente comando

python -m venv ambiente

* Luego, activamos el ambiente virtual

- En windows:
cd nombre_ambiente\Scripts
.\Activate

* De no funcionar, ejecutamos
Set-ExecutionPolicy Bypass -Scope CurrentUser

* Luego volvemos a la carpeta raíz
cd ..

- En linux:
source ./ambiente/bin/activate.fish

* Para desactivar el ambiente virtual:
deactivate

* Ahora, actualizaremos pip:
python -m pip install --upgrade pip

* Una vez actualizado, instalaremos django:
pip install django

* Crearemos el entorno de django, en este caso, core
django-admin startproject core .

* A continuación crearemos la aplicación
django-admin startapp byteclass

* Iniciamos el servidor
python manage.py runserver

* Ingresamos al local host desde la siugiente ip 
http://127.0.0.1:8000

* Una vez comprobado que el servidor funciona, realizaremos los siguientes ajustes iniciales

1. Agregaremos nuestra app a INSTALLED_APPS en ./core/settings.py
INSTALLED_APPS = [
    # apps de django
    'byteclass',
]
2. Dentro del directorio de nuestra app crearemos una carpeta llamada templates donde crearemos nuestro 404.html para el manejo de errores y una carpeta con el mismo nombre que la app, donde meteremos todas nuestras "plantillas", quedando tal que así

|-ambiente
|-byteclass
|   |-templates
|   |   |- byteclass
|   |   |   |- index.html (pantalla principal)
|   |   |
|   |   |- 404.html
|-core
|-...

