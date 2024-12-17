"""
URL configuration for miproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.principal, name='principal'),
    path('/listadoCursos', views.listar_cursos, name='listar_cursos'),
    path('/listadoEstudiantes', views.listar_estudiantes, name='listar_estudiantes'),
    path('/listadoInscripciones', views.listar_inscripciones, name='listar_inscripciones'),
    path('/editar_curso/<int:pk>', views.editar_curso, name='editar_curso'),
    path('/editar_estudiante/<int:pk>', views.editar_estudiante, name='editar_estudiante'),
    path('/editar_inscripcion/<int:pk>', views.editar_inscripcion, name='editar_inscripcion'),
    path('/crear_curso', views.crear_curso, name='crear_curso'),
    path('/crear_estudiante', views.crear_estudiante, name='crear_estudiante'),
    path('/crear_inscripcion', views.crear_inscripcion, name='crear_inscripcion'),
]
