from rest_framework import serializers 
from .models import Alumnos
 
 
class AlumnosSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Alumnos
        fields = ('id',
                  'nombres',  
                  'apellidos',
                  'matricula',
                  'carrera',                  
                  'semestre',
                  'correo',
                  'img',
                  'created',
                  'modified')