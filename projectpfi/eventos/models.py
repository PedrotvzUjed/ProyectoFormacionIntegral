from django.db import models

# Create your models here.
class eventos(models.Model):

    #Descripcion 
    unidadResponsable = models.CharField(max_length=50, blank=False,default='')
    tituloEvento = models.CharField(max_length=50,blank=False,default='')
    descripcionEvento = models.TextField()
    eventoDedicadoA = models.CharField(max_length=50)
    #imagen = models.ImageField()
    #Calendario
    fechaEvento = models.DateField()
    inicioEvento = models.TimeField()
    finEvento = models.TimeField()
    sede = models.CharField(max_length=100)
    cupo = models.IntegerField()
    descripcion = models.TextField()
    #Creditos
    creditos = models.DecimalField(max_digits = 3,decimal_places=2)
    categorias = models.CharField(max_length=50)
    