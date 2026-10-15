from django.urls import path, include
from byteclass import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'curso', views.CursoViewSet)
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'historial-conexion', views.HistorialConexionViewSet)
router.register(r'seccion', views.SeccionViewSet)
router.register(r'leccion', views.LeccionViewSet)
router.register(r'evaluacion', views.EvaluacionViewSet)
router.register(r'pregunta', views.PreguntaViewSet)
router.register(r'opcion', views.OpcionViewSet)
router.register(r'matricula', views.MatriculaViewSet)
router.register(r'progreso-leccion', views.ProgresoLeccionViewSet)
router.register(r'entrega-evaluacion', views.EntregaEvaluacionViewSet)
router.register(r'respuesta-estudiante', views.RespuestaEstudianteViewSet)
router.register(r'registro-auditoria', views.RegistroAuditoriaViewSet)
router.register(r'notificacion', views.NotificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]