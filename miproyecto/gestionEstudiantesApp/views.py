from django.shortcuts import get_object_or_404, redirect, render
from .models import Curso,Estudiante,Inscripcion
from .forms import curso_form,estudiante_form,inscripcion_form
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

def editar_curso(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    if request.method == 'POST':
        form = curso_form(request.POST,instance=curso)
        if form.is_valid():
            form.save()
            cursos = Curso.objects.all()
            return render(request,'gestionEstudiantesApp/listarCursos.html',{"cursos":cursos})
    else:
        form = curso_form(instance=curso)
    return render(request, 'gestionEstudiantesApp/editarCursos.html',{"form":form,"pk":pk})
    
def editar_estudiante(request,pk):
    estudiante = get_object_or_404(Estudiante,pk=pk)
    if request.method == 'POST':
        form = estudiante_form(request.POST,instance=estudiante)
        if form.is_valid():
            form.save()
            estudiantes = Estudiante.objects.all()
            return render(request,'gestionEstudiantesApp/listarEstudiantes.html',{"estudiantes":estudiantes})
    else:
        form = estudiante_form(instance=estudiante)
    return render(request, 'gestionEstudiantesApp/editarEstudiantes.html',{"form":form,"pk":pk})


def editar_inscripcion(request,pk):
    inscripcion = get_object_or_404(Inscripcion,pk=pk)
    if request.method == 'POST':
        form = inscripcion_form(request.POST,instance=inscripcion)
        if form.is_valid():
            form.save()
            inscripciones = Inscripcion.objects.all()
            return render(request,'gestionEstudiantesApp/listarInscripciones.html',{"inscripciones":inscripciones})
    else:
        form = inscripcion_form(instance=inscripcion)
    return render(request, 'gestionEstudiantesApp/editarInscripciones.html',{"form":form,"pk":pk})


def delete_curso(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('principal')
    else:
        form = curso_form(instance=curso)
    return render(request, 'gestionEstudiantesApp/curso_delete_confirm.html',{"form":form,"curso":curso})

def delete_estudiante(request,pk):
    estudiante = get_object_or_404(Estudiante,pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('principal')
    else:
        form = curso_form(instance=estudiante)
    return render(request, 'gestionEstudiantesApp/estudiante_delete_confirm.html',{"form":form,"estudiante":estudiante})

def delete_inscripcion(request,pk):
    inscripcion = get_object_or_404(Inscripcion,pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('principal')
    else:
        form = curso_form(instance=inscripcion)
    return render(request, 'gestionEstudiantesApp/inscripcion_delete_confirm.html',{"form":form,"inscripcion":inscripcion})

def crear_curso(request):
    if request.method == 'POST':
        form = curso_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = curso_form()
    return render(request, 'gestionEstudiantesApp/curso_new.html',{"form":form})

def crear_estudiante(request):
    if request.method == 'POST':
        form = estudiante_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = estudiante_form()
    return render(request, 'gestionEstudiantesApp/estudiante_new.html',{"form":form})

def crear_inscripcion(request):
    if request.method == 'POST':
        form = inscripcion_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = inscripcion_form()
    return render(request, 'gestionEstudiantesApp/inscripcion_new.html',{"form":form})