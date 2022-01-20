from django.db import models
from rest_framework import serializers 
from .models import eventos, eventosCalendario, eventosSubirevidenciasAlumno
 
 
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

    class Meta:
        model = eventosCalendario
        fields = ('id',
                  'name',  
                  'color',
                  'start',
                  'end',
                  'details',
                  'evento')
        
        #fields = '__all__'

class evidenciaSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = eventosSubirevidenciasAlumno
        fields = (
                  'img',
                  'evento',
                  'alumno'
        )

class evidenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = eventosSubirevidenciasAlumno
        fields = ('id',
                  'img',
                  'evento',
                  'alumno')