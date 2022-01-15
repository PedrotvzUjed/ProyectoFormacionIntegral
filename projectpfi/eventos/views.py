from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import eventos, eventosCalendario, eventosSubirevidenciasAlumno
from .serializers import eventosSerializer, calendarioSerializer, evidenciaSerializer
from rest_framework.decorators import api_view

from rest_framework import generics
import django_filters.rest_framework

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

#RetrieveUpdateDestroyAPIView

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

#Subir evidencias de alumnos
class evidenciasCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = eventosSubirevidenciasAlumno.objects.all(),
    serializer_class = evidenciaSerializer

class evidenciasList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = eventosSubirevidenciasAlumno.objects.all()
    serializer_class = evidenciaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['id', 'evento', 'alumno']
