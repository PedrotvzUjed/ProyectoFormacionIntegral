from rest_framework import serializers 
from .models import eventos
 
 
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