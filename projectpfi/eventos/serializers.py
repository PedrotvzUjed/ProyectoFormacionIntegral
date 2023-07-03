from django.db import models
from rest_framework import serializers 
from .models import eventos, eventosCalendario, eventosSubirevidenciasAlumno
from eventos.models import *
 
class eventosSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = eventos
        fields = '__all__'
        
class eventosEditSerializer(serializers.ModelSerializer):
    categorias = serializers.SerializerMethodField()
    subCategoria1 = serializers.SerializerMethodField()
    subCategoria2 = serializers.SerializerMethodField()
    subCategoriaArte = serializers.SerializerMethodField()
    
    class Meta:
        model = eventos
        fields = '__all__'
    
    def get_categorias(self, obj):
        return {
            'id' : obj.categorias.id,
            'text': obj.categorias.text
        }
    
    def get_subCategoria1(self, obj):
        return {
            'id' : obj.subCategoria1.id,
            'text': obj.subCategoria1.text,
            'clasificacion': obj.subCategoria1.clasificacion_id,
            'objetivo': obj.subCategoria1.objetivo
        }
    def get_subCategoria2(self, obj):
        try:
            return {
                'id' : obj.subCategoria2.id,
                'text': obj.subCategoria2.text,
                'catalogo': obj.subCategoria2.catalogo_id
            }
        except:
            return ''
    
    def get_subCategoriaArte(self, obj):
        try: 
            return {
            'id' : obj.subCategoriaArte.id,
            'text': obj.subCategoriaArte.text,
            'categoria': obj.subCategoriaArte.categoria_id
            }
        except:
            return ''
             
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

class CategoriasArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = arte_categorias
        fields = '__all__'
