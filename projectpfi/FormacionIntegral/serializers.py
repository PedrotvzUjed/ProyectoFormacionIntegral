from rest_framework import serializers 
from .models import FormacionIntegral
 
 
class FormacionInSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FormacionIntegral
        fields = ('id',
                  'nombre',  
                  'matricula',
                  'asistencia',
                  'evento_id',
                  'alumno_id',
                  'created',
                  'modified')
        
        #fields = '__all__'