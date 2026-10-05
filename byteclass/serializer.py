from rest_framework import serializers

from .models import Usuario
from .models import Curso
from .models import HistorialConexion
from .models import Curso
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

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = 'codigo', 'periodo', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = 'titulo', 'descripcion'

class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = 'titulo', 'tipo', 'contenido_texto', 'url', 'archivo'

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'tipo', 'estado'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = 'texto', 'tipo', 'puntaje'

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = 'texto', 'es_correcta'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = 'id_curso', 'id_estudiante', 'fecha_matricula'

class ProgresoLeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoLeccion
        fields = 'id_leccion', 'id_estudiante', 'completado'

class EntregaEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntregaEvaluacion
        fields = 'id_evaluacion', 'id_estudiante', 'fecha_entrega', 'puntaje_obtenido'

class RespuestaEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaEstudiante
        fields = 'id_entrega_evaluacion', 'id_pregunta', 'id_opcion', 'texto_abierto', 'puntaje_obtenido'

class RegistroAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAuditoria
        fields = 'usuario', 'accion', 'fecha', 'detalle'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = 'id_usuario', 'mensaje', 'fecha_envio', 'leida'

class HistorialConexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialConexion
        fields = 'id_usuario', 'fecha_conexion'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = 'username', 'nombre', 'apellido', 'correo_institucional', 'rol_principal'


