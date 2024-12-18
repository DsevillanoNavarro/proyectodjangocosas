from datetime import date
from django import forms
from django.forms import ModelForm, Textarea, ValidationError
from gestionEstudiantesApp.models import Curso,Estudiante,Inscripcion

class curso_form(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            }
class estudiante_form(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            }
class inscripcion_form(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        widgets = {
            'fecha_inscripcion': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }