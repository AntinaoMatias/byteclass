"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from byteclass import views
from django.contrib.auth import views as auth_views

"""
Se configuró, adicionalmente, la ruta para /api/
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='inicio'),
    path('byteclass/', include('byteclass.urls')),
    path('api/', include('byteclass.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('pagina_inicio/', views.pagina_inicio, name='pagina_inicio'),
    path('curso/<int:curso_id>/', views.CursoDetalleView.as_view(), name='detalle_curso'),
    path('404/', views.error_404, name='error_404'),
]
