from django.contrib import admin

# Register your models here.
from .models import Estudiante, Inscripcion, Curso
# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Inscripcion)