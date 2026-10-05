from django.urls import path, include
from rest_framework import routers
from byteclass import views

router = routers.DefaultRouter()
router.register(r'Curso', views.CursoViewSet)
router.register(r'Usuario', views.UsuarioViewSet)
router.register(r'HistorialConexion', views.HistorialConexionViewSet)
router.register(r'Seccion', views.SeccionViewSet)
router.register(r'Leccion', views.LeccionViewSet)
router.register(r'Evaluacion', views.EvaluacionViewSet)
router.register(r'Pregunta', views.PreguntaViewSet)
router.register(r'Opcion', views.OpcionViewSet)
router.register(r'Matricula', views.MatriculaViewSet)
router.register(r'ProgresoLeccion', views.ProgresoLeccionViewSet)
router.register(r'EntregaEvaluacion', views.EntregaEvaluacionViewSet)



urlpatterns = [
    path('', include(router.urls))
]