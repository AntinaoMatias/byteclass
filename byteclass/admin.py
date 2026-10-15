from django.contrib import admin

import byteclass

from .models import Curso, EntregaEvaluacion, Evaluacion, HistorialConexion, Leccion, Matricula, Notificacion, Opcion, Pregunta, ProgresoLeccion, RegistroAuditoria, RespuestaEstudiante, Seccion, Usuario

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
