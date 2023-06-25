from django.db import models
from django.db.models.deletion import CASCADE
from Alumnos.models import Alumnos
# Create your models here.
class eventos(models.Model):

    #Descripcion 
    unidadResponsable = models.CharField('unidadResponsable', max_length=150, blank=False,default='')
    tituloEvento = models.CharField('tituloEvento', max_length=200,blank=False,default='')
    descripcionEvento = models.TextField('descripcionEvento')
    eventoDedicadoA = models.CharField('eventoDedicadoA', max_length=200)
    #imagen = models.ImageField(upload_to='Eventos/images')
    #Calendario
    fechaEvento = models.DateField('fechaEvento')
    inicioEvento = models.TimeField('inicioEvento',)
    finEvento = models.TimeField('finEvento',)
    sede = models.CharField('sede', max_length=150)
    cupo = models.IntegerField('cupo')
    descripcion = models.TextField('descripcion')
    #Creditos
    creditos = models.DecimalField('creditos', max_digits = 3,decimal_places=2)
    categorias = models.CharField('categorias', max_length=100)
    
#modelo para el modulo calendario de eventos
class eventosCalendario(models.Model):

    name = models.CharField('name', max_length=200)
    color = models.CharField('color', max_length=100)
    start = models.CharField('start', max_length=200)
    end = models.CharField('end', max_length=200)
    details = models.CharField('details', max_length=250)
    evento = models.ForeignKey(eventos, on_delete=models.CASCADE)

class eventosSubirevidenciasAlumno(models.Model):
    img = models.ImageField(upload_to='EvidenciasAlumnos/images')
    evento = models.ForeignKey(eventos, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumnos, on_delete=CASCADE)

class clasifi_cat(models.Model):
    text = models.CharField(max_length = 100)

class catalogo_categorias(models.Model):
    text = models.CharField(max_length = 100)
    clasificacion = models.ForeignKey(clasifi_cat, on_delete=CASCADE, null= True)

class catalogo_categorias2(models.Model):
    text = models.CharField(max_length = 100)
    catalogo = models.ForeignKey(catalogo_categorias, on_delete=CASCADE, null= True)

class catalogo_civismo(models.Model):
    text = models.CharField(max_length = 100)
    clasificacion = models.ForeignKey(clasifi_cat, on_delete=CASCADE, null= True)

class catalogo_registro_civismo(models.Model):
    text = models.CharField(max_length = 100)
    catalogo = models.ForeignKey(catalogo_civismo, on_delete=CASCADE, null= True)

class catalogo_deporte(models.Model):
    text = models.CharField(max_length = 100)
    clasificacion = models.ForeignKey(clasifi_cat, on_delete=CASCADE, null= True)

class categorias_deporte(models.Model):
    text = models.CharField(max_length = 100)
    catalogo = models.ForeignKey(catalogo_deporte, on_delete=CASCADE, null= True)

class catalogo_ciencia(models.Model):
    text = models.CharField(max_length = 100)
    clasificacion = models.ForeignKey(clasifi_cat, on_delete=CASCADE, null= True)

class categorias_ciencia(models.Model):
    text = models.CharField(max_length = 100)
    catalogo = models.ForeignKey(catalogo_ciencia, on_delete=CASCADE, null= True)


