from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario
from .models import Curso
from .models import HistorialConexion
from .models import Seccion
from .models import Leccion
from .models import Evaluacion
from .models import Pregunta
from .models import Opcion
from .models import Matricula
from .models import ProgresoLeccion
from .models import EntregaEvaluacion
from .models import RespuestaEstudiante
from .models import RegistroAuditoria
from .models import Notificacion

from .serializer import UsuarioSerializer
from .serializer import CursoSerializer
from .serializer import HistorialConexionSerializer
from .serializer import SeccionSerializer
from .serializer import LeccionSerializer
from .serializer import EvaluacionSerializer
from .serializer import PreguntaSerializer
from .serializer import OpcionSerializer
from .serializer import MatriculaSerializer
from .serializer import ProgresoLeccionSerializer
from .serializer import EntregaEvaluacionSerializer
from .serializer import RespuestaEstudianteSerializer
from .serializer import RegistroAuditoriaSerializer
from .serializer import NotificacionSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class HistorialConexionViewSet(viewsets.ModelViewSet):
    queryset = HistorialConexion.objects.all()
    serializer_class = HistorialConexionSerializer

class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer

class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class OpcionViewSet(viewsets.ModelViewSet):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ProgresoLeccionViewSet(viewsets.ModelViewSet):
    queryset = ProgresoLeccion.objects.all()
    serializer_class = ProgresoLeccionSerializer

class EntregaEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = EntregaEvaluacion.objects.all()
    serializer_class = EntregaEvaluacionSerializer

class RespuestaEstudianteViewSet(viewsets.ModelViewSet):
    queryset = RespuestaEstudiante.objects.all()
    serializer_class = RespuestaEstudianteSerializer

class RegistroAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAuditoria.objects.all()
    serializer_class = RegistroAuditoriaSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer




# Create your views here.

def bienvenida(request):
    return render(request, 'byteclass/index.html')

def error_404(request, exception):
    return render(request, 'byteclass/404.html', status=404)