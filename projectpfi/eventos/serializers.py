from rest_framework import serializers 
from .models import eventos, eventosCalendario 
 
 
class eventosSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = eventos
        fields = ('id',
                  'unidadResponsable',  
                  'tituloEvento',
                  'descripcionEvento',
                  'eventoDedicadoA',
                  #'imagen',
                  
                  'fechaEvento',
                  'inicioEvento',
                  'finEvento',
                  'sede',
                  'cupo',
                  'descripcion',
                  'creditos',
                  'categorias')
        
        #fields = '__all__'

class calendarioSerializer(serializers.ModelSerializer):
    tituloEvento = serializers.CharField(source = 'evento.tituloEvento')
    class Meta:
        model = eventosCalendario
        fields = ('id',
                  'name',  
                  'color',
                  'start',
                  'end',
                  'details',
                  'evento',
                  'tituloEvento')
        
        #fields = '__all__'