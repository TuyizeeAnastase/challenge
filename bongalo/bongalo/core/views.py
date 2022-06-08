import imp
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SpaceSerialize
from .models import Space

# Create your views here.

class ViewSpace(viewsets.ModelViewSet):
    serializer_class = SpaceSerialize
    queryset = Space.objects.all()

