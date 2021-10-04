from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import FormacionIntegral
from .serializers import formacionSerializer
from rest_framework.decorators import api_view

from rest_framework import generics

class registroInCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = FormacionIntegral.objects.all(),
    serializer_class = formacionSerializer

class registroInList(generics.ListAPIView):
    # API endpoint that allows creation of a new customer
    queryset = FormacionIntegral.objects.all(),
    serializer_class = formacionSerializer

class registroInDetail(generics.RetrieveAPIView):
    # API endpoint that allows creation of a new customer
    queryset = FormacionIntegral.objects.all(),
    serializer_class = formacionSerializer

class registroInUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = FormacionIntegral.objects.all(),
    serializer_class = formacionSerializer

class registroInDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows creation of a new customer
    queryset = FormacionIntegral.objects.all(),
    serializer_class = formacionSerializer