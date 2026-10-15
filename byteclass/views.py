from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class HistorialConexionViewSet(viewsets.ModelViewSet):
    queryset = HistorialConexion.objects.all()
    serializer_class = HistorialConexionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class OpcionViewSet(viewsets.ModelViewSet):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class ProgresoLeccionViewSet(viewsets.ModelViewSet):
    queryset = ProgresoLeccion.objects.all()
    serializer_class = ProgresoLeccionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class EntregaEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = EntregaEvaluacion.objects.all()
    serializer_class = EntregaEvaluacionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class RespuestaEstudianteViewSet(viewsets.ModelViewSet):
    queryset = RespuestaEstudiante.objects.all()
    serializer_class = RespuestaEstudianteSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class RegistroAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAuditoria.objects.all()
    serializer_class = RegistroAuditoriaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]




# Create your views here.

def bienvenida(request):
    return render(request, 'byteclass/index.html')

def error_404(request, exception):
    return render(request, 'byteclass/404.html', status=404)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('pagina_inicio')
        else:
            messages.error(request, "No ha sido posible registrarte. Por favor revisa los errores indicados.")
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def pagina_inicio(request):
    request.session['mensaje_bienvenida'] = f'¡Bienvenido a byteclass, {request.user.username}!'
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']

    cursos = Curso.objects.all()

    return render(request, 'byteclass/pagina_inicio.html', {
        'cursos': cursos,
        'message': mensaje_bienvenida,
    })

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

@login_required
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'byteclass/detalle_curso.html', {'curso': curso})

