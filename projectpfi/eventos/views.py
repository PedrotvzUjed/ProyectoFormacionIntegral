from django.shortcuts import render,  get_object_or_404
from rest_framework import status
 
from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import exceptions
import django_filters.rest_framework

#Eventos
class eventosCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = eventos.objects.all(),
    serializer_class = eventosSerializer


class eventosList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = eventos.objects.all()
    serializer_class = eventosSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['id', 'creditos', 'fechaEvento', 'categorias']

...
class eventosDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = eventos.objects.all()
    serializer_class = eventosSerializer

    ...
class eventosUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = eventos.objects.all()
    serializer_class = eventosSerializer

class eventosDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = eventos.objects.all()
    serializer_class = eventosSerializer

#Clases de calendario
class calendarioCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = eventosCalendario.objects.all(),
    serializer_class = calendarioSerializer

class calendarioList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = eventosCalendario.objects.all()
    serializer_class = calendarioSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['id', 'start', 'evento']

class ClasificacionEventosList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = clasifi_cat.objects.all()
    serializer_class = clasificacionSerializer

class Categorias1List(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = catalogo_categorias.objects.all()
    serializer_class = Categorias1Serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['clasificacion']

class Categorias2List(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = catalogo_categorias2.objects.all()
    serializer_class = Categorias2Serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['catalogo']


class CatalogoCivismoList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = catalogo_civismo.objects.all()
    serializer_class = catalogoCivSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['clasificacion']

class CategoriaCivismoList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = catalogo_registro_civismo.objects.all()
    serializer_class = categoriaCivSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['catalogo']

class CatalogoDepList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = catalogo_deporte.objects.all()
    serializer_class = catalogoDepSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['clasificacion']

class CategoriaDepList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = categorias_deporte.objects.all()
    serializer_class = categoriaDepSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['catalogo']

class CatalogoCienciaList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = catalogo_ciencia.objects.all()
    serializer_class = catalogoCienciaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['clasificacion']

class CategoriaCienciaList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = categorias_ciencia.objects.all()
    serializer_class = categoriaCienciaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['catalogo']

#evidencias de alumnos
class evidencias(APIView):        
    def post(self, request):
        if 'img' not in request.data:
            raise exceptions.ParseError("No has seleccionado el archivo a subir")
        
        archivos = str(request.FILES)
        print(request.data)
        serializer = evidenciaSerializerCreate(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            evidencia = eventosSubirevidenciasAlumno(**validated_data)
            evidencia.save()

            serializer_response = evidenciaSerializerCreate(evidencia)    
           
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class evidenciasUpdate(APIView):
    def get_object(self, pk):
        evidencia = get_object_or_404(eventosSubirevidenciasAlumno, pk=pk)
        return evidencia

    def put(self, request, pk):
        evidencia = self.get_object(pk)
        
        serializer = evidenciaSerializer(evidencia,data=request.data)

        if(serializer.is_valid()):
            evidencia = eventosSubirevidenciasAlumno(**serializer.validated_data)
            evidencia.pk = pk
            evidencia.save(update_fields=['img'])
            evidencia = eventosSubirevidenciasAlumno.objects.get(pk=pk)
            serializer_response  = evidenciaSerializer(evidencia)
            return Response(serializer_response.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class evidenciasList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = eventosSubirevidenciasAlumno.objects.all()
    serializer_class = evidenciaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['id', 'evento', 'alumno']
