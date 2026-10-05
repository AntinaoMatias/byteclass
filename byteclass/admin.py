from django.contrib import admin

import byteclass

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



# Register your models here.

from rest_framework import serializers

admin.site.register(Usuario)
admin.site.register(Curso)
admin.site.register(HistorialConexion)
admin.site.register(Seccion)
admin.site.register(Leccion)
admin.site.register(Evaluacion)
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Matricula)
admin.site.register(ProgresoLeccion)
admin.site.register(EntregaEvaluacion)
admin.site.register(RespuestaEstudiante)
admin.site.register(RegistroAuditoria)
admin.site.register(Notificacion)
