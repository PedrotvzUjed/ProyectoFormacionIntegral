from django.db import models
from eventos.models import eventos
from Alumnos.models import Alumnos

# Create your models here.
class FormacionIntegral(models.Model):
    nombre = models.CharField('nombre', max_length=150)
    matricula = models.CharField('matricula', max_length=10)
    asistencia = models.IntegerField('asistencia', null=True, default=0)
    evento = models.ForeignKey(eventos, null=True, verbose_name='evento_id', on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumnos, null=True, verbose_name='alumno_id', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)