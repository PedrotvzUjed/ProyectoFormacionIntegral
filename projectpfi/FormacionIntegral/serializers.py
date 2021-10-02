from rest_framework import serializers 
from .models import FormacionIntegral
 
 
class formacionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FormacionIntegral
        fields = ('id',
                  'nombre',  
                  'matricula',
                  'asistencia',
                  'evento_id')