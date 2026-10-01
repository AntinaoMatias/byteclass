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