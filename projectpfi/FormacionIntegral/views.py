from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import FormacionIntegral
from .serializers import FormacionInSerializer
from rest_framework.decorators import api_view

from rest_framework import generics
import django_filters.rest_framework

class FormacionInCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = FormacionIntegral.objects.all(),
    serializer_class = FormacionInSerializer


class FormacionInList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['evento_id']

...
class FormacionInDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer

    ...
class FormacionInUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer

class FormacionInDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer

#RetrieveUpdateDestroyAPIView
