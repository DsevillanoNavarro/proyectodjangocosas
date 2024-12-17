from datetime import date
from django.db import models
from django.forms import ValidationError

# Create your models here.
class Curso(models.Model):
    nombre = models.TextField(max_length=100)
    codigo = models.TextField(unique=True, max_length=10)
    fecha_inicio=models.DateField()
    fecha_fin= models.DateField()
    
    def Clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError("La fecha de inicio a de ser anterior a la fecha fin")
        return super().clean()
class Estudiante(models.Model):
    nombre = models.TextField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento= models.DateField()
    
    def Clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento tiene que ser anterior al día actual")
        mayor_de_edad = (date.today()-self.fecha_nacimiento).days // 365.25
        if mayor_de_edad < 18:
            raise ValidationError("Tiene que tener 18 años")
        return super().clean()
        
    
class Inscripcion(models.Model):
    estudiante= models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="estudiantes")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="curso")
    fecha_inscripcion = models.DateField()
    
    def Clean(self):
        if self.fecha_inscripcion > self.curso.fecha_fin:
            raise ValidationError("El curso al que intenta inscribirse ha terminado")
        if self.fecha_inscripcion > date.today():
            raise ValidationError("La fecha de inscripcion tiene que ser anterior al día actual")
        return super().clean()