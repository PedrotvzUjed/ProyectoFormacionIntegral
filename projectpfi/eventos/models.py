from django.db import models
from django.db.models.deletion import CASCADE
from Alumnos.models import Alumnos
# Create your models here.
class clasifi_cat(models.Model):
    text = models.CharField(max_length = 100)

class catalogo_categorias(models.Model):
    text = models.CharField(max_length = 100)
    clasificacion = models.ForeignKey(clasifi_cat, on_delete=CASCADE, null= True)

class catalogo_categorias2(models.Model):
    text = models.CharField(max_length = 100)
    catalogo = models.ForeignKey(catalogo_categorias, on_delete=CASCADE, null= True)

class arte_categorias(models.Model):
    text = models.CharField(max_length = 100)
    categoria = models.ForeignKey(catalogo_categorias2, on_delete=CASCADE, null= True)

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
    categorias = models.ForeignKey(clasifi_cat, on_delete=models.CASCADE, related_name='categorias')
    subCategoria1 = models.ForeignKey(catalogo_categorias, on_delete=models.CASCADE, null= True, related_name='categorias1')
    subCategoria2 = models.ForeignKey(catalogo_categorias2, on_delete=models.CASCADE, null= True, related_name='categorias2')
    subCategoriaArte = models.ForeignKey(arte_categorias, on_delete=models.CASCADE, null= True, related_name='categoriasArte')

    
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



