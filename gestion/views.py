from django.shortcuts import render
from rest_framework import viewsets
from .models import Autor, Libro # IMPORT MY MODELS
from .serializers import AutorSerializer, LibroSerializer #IMPORT SERIALIZERS 
from rest_framework.exceptions import ValidationError

# Create your views here.


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    # Validación para evitar eliminar autores con libros asociados
    def perform_destroy(self, instance):
        if instance.libro_set.exists():
            raise ValidationError("No se puede eliminar un autor con libros asociados.")
        instance.delete()

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer