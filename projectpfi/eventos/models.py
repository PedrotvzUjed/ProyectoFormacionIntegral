from django.db import models

# Create your models here.
class eventos(models.Model):

    #Descripcion 
    unidadResponsable = models.CharField('unidadResponsable', max_length=50, blank=False,default='')
    tituloEvento = models.CharField('tituloEvento', max_length=50,blank=False,default='')
    descripcionEvento = models.TextField('descripcionEvento')
    eventoDedicadoA = models.CharField('eventoDedicadoA', max_length=50)
    #imagen = models.ImageField(upload_to='Eventos/images')
    #Calendario
    fechaEvento = models.DateField('fechaEvento')
    inicioEvento = models.TimeField('inicioEvento',)
    finEvento = models.TimeField('finEvento',)
    sede = models.CharField('sede', max_length=100)
    cupo = models.IntegerField('cupo')
    descripcion = models.TextField('descripcion')
    #Creditos
    creditos = models.DecimalField('creditos', max_digits = 3,decimal_places=2)
    categorias = models.CharField('categorias', max_length=50)
    
#modelo para el modulo calendario de eventos
class eventosCalendario(models.Model):

    name = models.CharField('name', max_length=50)
    color = models.CharField('color', max_length=20)
    start = models.CharField('start', max_length=50)
    end = models.CharField('end', max_length=50)
    details = models.CharField('details', max_length=60)
    evento = models.ForeignKey(eventos, on_delete=models.CASCADE)