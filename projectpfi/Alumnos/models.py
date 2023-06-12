from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombres = models.CharField('nombres', max_length=80)
    apellidos = models.CharField('apellidos', max_length=80)
    matricula = models.CharField('matricula', max_length=50)
    carrera = models.CharField('carrera', max_length=50)
    semestre = models.IntegerField('semestre') 
    correo = models.EmailField('correo', max_length=50)
    contraseña = models.CharField('contraseña', max_length=50)
    img = models.ImageField(upload_to='Alumnos/images')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)