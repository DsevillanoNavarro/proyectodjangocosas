from datetime import date
from django import forms
from django.forms import ModelForm, Textarea, ValidationError
from gestionEstudiantesApp.models import Curso,Estudiante,Inscripcion

class curso_form(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
class estudiante_form(forms.Form):
    class Meta:
        model = Estudiante
        fields = '__all__'
class inscripcion_form(forms.Form):
    class Meta:
        model = Inscripcion
        fields = '__all__'