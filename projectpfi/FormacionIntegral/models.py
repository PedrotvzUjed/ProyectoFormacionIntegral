from django.db import models
from eventos.models import eventos
from Alumnos.models import Alumnos

# Create your models here.
class FormacionIntegral(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    matricula = models.IntegerField('matricula')
    asistencia = models.IntegerField('asistencia', null=True)
    evento_id = models.ForeignKey(eventos, null=True, verbose_name='evento', on_delete=models.CASCADE)
    alumno_id = models.ForeignKey(Alumnos, null=True, verbose_name='alumno', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)