from django.shortcuts import render

from .models import Pelicula
from .serializers import PeliculaSerializer
from rest_framework import viewsets

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer