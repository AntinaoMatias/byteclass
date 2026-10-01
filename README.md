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

3. En el archivo ./byteclass/views.py crearemos la función que llevará a nuestros html

def bienvenida(request):
    return render(request, 'index.html')

def error_404(request, exception):
    return render(request, 'byteclass/404.html', status=404)

4. Importamos las vistas a ./core/urls.py y llamamos al método que las va a renderizar (path)

from byteclass import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('404/', views.error_404, name='error_404'),
]

5. Para que nuestra págian de error funcione correctamente y no dé información sensible a los usuarios, deshabilitaremos el modo debug y autorizaremos localhost y 127.0.0.1 en settings.py

DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1']

* Para el modelado de datos realizaremos los siguientes ajustes

1. Crear tablas django en la base de datos:
python manage.py migrate

2. Crear una nueva migración, que será la nuestra:
python manage.py makemigrations

3. Aplicamos la migración a la base de datos:
python manage.py migrate

Cada vez que modifiquemos el modelo de datos, crearemos una nueva migración y la aplicaremos a la base de datos para que se actualice de acuerdo anuestro modelo.

* Estructura de una clase:
class MiModelo(models.Model):
    atributo_1 = models.CharField(max_length=25,null=false)
    atributo_2 = models.TextField(max_length=100,null=false)
    atributo_3 = models.DateField(null=false)
    atributo_4 = models.TimeField(null=false)
    atributo_5 = models.DateTimeField(max_length=100,null=false)
    atributo_6 = models.IntegerField()
    atributo_7 = models.DecimalField()
    atributo_8 = models.FloatField()
    atributo_9 = models.EmailField()
    atributo_10 = models.BooleanField(default=true)
    atributo_11 = models.URLField(default=true)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

class MiModelo2(models.Model):
    atributo_referenciado = models.ForeignKey(MiModelo,on_delete=CASCADE)
    atributo_2 = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

* 