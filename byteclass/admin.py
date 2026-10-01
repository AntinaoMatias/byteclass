from django.contrib import admin

import byteclass

from byteclass.models import Usuario
from byteclass.models import Curso
from byteclass.models import HistorialConexion
from byteclass.models import Curso
from byteclass.models import Seccion
from byteclass.models import Leccion
from byteclass.models import Evaluacion
from byteclass.models import Pregunta
from byteclass.models import Opcion
from byteclass.models import Matricula
from byteclass.models import ProgresoLeccion
from byteclass.models import EntregaEvaluacion
from byteclass.models import RespuestaEstudiante
from byteclass.models import RegistroAuditoria
from byteclass.models import Notificacion



# Register your models here.

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