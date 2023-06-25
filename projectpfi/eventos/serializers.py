from django.db import models
from rest_framework import serializers 
from .models import eventos, eventosCalendario, eventosSubirevidenciasAlumno
from eventos.models import *
 
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

class clasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = clasifi_cat
        fields = '__all__'

class Categorias1Serializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo_categorias
        fields = '__all__'

class Categorias2Serializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo_categorias2
        fields = '__all__'


class catalogoCivSerializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo_civismo
        fields = '__all__'


class categoriaCivSerializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo_registro_civismo
        fields = '__all__'

class catalogoCienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo_ciencia
        fields = '__all__'


class categoriaCienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorias_ciencia
        fields = '__all__'

class catalogoDepSerializer(serializers.ModelSerializer):
    class Meta:
        model = catalogo_deporte
        fields = '__all__'


class categoriaDepSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorias_ciencia
        fields = '__all__'
