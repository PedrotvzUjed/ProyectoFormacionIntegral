from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Alumnos
from .serializers import AlumnosSerializer
from rest_framework.decorators import api_view

from rest_framework import generics

class AlumnosCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Alumnos.objects.all(),
    serializer_class = AlumnosSerializer


class AlumnosList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer

...
class AlumnosDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer

    ...
class AlumnosUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer

class AlumnosDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer