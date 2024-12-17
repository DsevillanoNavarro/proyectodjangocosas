from django.shortcuts import render
from .models import Curso,Estudiante,Inscripcion
# Create your views here.
def principal(request):
    return render(request,'gestionEstudiantesApp/principal.html')
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request,'gestionEstudiantesApp/listarCursos.html',{"cursos":cursos})
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'gestionEstudiantesApp/listarEstudiantes.html',{"estudiantes":estudiantes})
def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request,'gestionEstudiantesApp/listarInscripciones.html',{"inscripciones":inscripciones})
def crear_curso(request):
    return render(request,'gestionEstudiantesApp/crearCurso.html')
def crear_estudiante(request):
    return render(request,'gestionEstudiantesApp/crearEstudiante.html')
def crear_inscripcion(request):
    return render(request,'gestionEstudiantesApp/crearInscripcion.html')