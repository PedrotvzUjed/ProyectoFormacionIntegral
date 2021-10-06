from rest_framework import serializers 
from .models import FormacionIntegral
 
 
class FormacionInSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FormacionIntegral
        fields = ('id',
                  'nombre',  
                  'matricula',
                  'asistencia',
                  'evento',
                  'alumno',
                  'created',
                  'modified')
        
        #fields = '__all__'