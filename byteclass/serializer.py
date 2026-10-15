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

from rest_framework import serializers

from .models import (
    Usuario,
    Curso,
    Seccion,
    Leccion,
    Evaluacion,
    Pregunta,
    Opcion,
    Matricula,
    ProgresoLeccion,
    EntregaEvaluacion,
    RespuestaEstudiante,
    RegistroAuditoria,
    Notificacion,
    HistorialConexion,
)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'username',
            'nombre',
            'apellido',
            'rut',
            'correo_institucional',
            'telefono',
            'rol_principal',
            'habilitado',
        )
        extra_kwargs = {
            'contrasenia': {'write_only': True, 'required': False}
        }


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'codigo',
            'periodo',
            'titulo',
            'descripcion',
            'estado',
            'fecha_inicio',
            'fecha_fin',
            'id_instructor',
        )


class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = (
            'id',
            'titulo',
            'descripcion',
            'orden',
            'visibilidad',
            'id_curso',
        )


class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = (
            'id',
            'titulo',
            'tipo',
            'orden',
            'contenido_texto',
            'url',
            'archivo',
            'visibilidad',
            'id_seccion',
        )


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = (
            'id',
            'titulo',
            'descripcion',
            'estado',
            'visibilidad',
            'fecha_inicio',
            'fecha_limite',
            'puntaje_maximo',
            'id_seccion',
        )


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = (
            'id',
            'enunciado',
            'tipo_pregunta',
            'puntaje',
            'id_evaluacion',
        )


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = (
            'id',
            'texto',
            'es_correcta',
            'id_pregunta',
        )


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = (
            'id',
            'estado',
            'nota_final',
            'fecha_inscripcion',
            'id_curso',
            'id_estudiante',
        )


class ProgresoLeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoLeccion
        fields = (
            'id',
            'completada',
            'cantidad_accesos',
            'ultimo_acceso',
            'fecha_completado',
            'id_matricula',
            'id_leccion',
        )


class EntregaEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntregaEvaluacion
        fields = (
            'id',
            'estado_calificacion',
            'nota',
            'aprobado',
            'fecha_entrega',
            'numero_intento',
            'id_evaluacion',
            'id_matricula',
        )


class RespuestaEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaEstudiante
        fields = (
            'id',
            'texto_abierto',
            'retroalimentacion',
            'puntaje_obtenido',
            'id_entrega_evaluacion',
            'id_pregunta',
            'id_opcion',
        )


class HistorialConexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialConexion
        fields = (
            'id',
            'fechahora_ingreso',
            'fechahora_salida',
            'id_usuario',
        )


class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = (
            'id',
            'titulo',
            'mensaje',
            'fecha',
            'leido',
            'id_curso',
            'id_usuario_emisor',
            'id_usuario_receptor',
        )


class RegistroAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAuditoria
        fields = (
            'id',
            'accion',
            'tabla_afectada',
            'id_registro_modificado',
            'estado_anterior',
            'estado_nuevo',
            'fecha_modificacion',
            'id_usuario',
        )