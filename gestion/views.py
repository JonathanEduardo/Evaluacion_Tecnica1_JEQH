from django.shortcuts import render
from rest_framework import viewsets
from .models import Autor, Libro # import modelos
from .serializers import AutorSerializer, LibroSerializer #Import serlializers 
from rest_framework.exceptions import ValidationError # Import validation error


# Create your views here.

# ViewSet for the Autor model
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()  # Get all Autor objects
    serializer_class = AutorSerializer  # Use AutorSerializer for serialization

 # Validation to prevent deleting authors with associated books
    def perform_destroy(self, instance):
        if instance.libro_set.exists(): # Check if the author has associated books
            raise ValidationError("No se puede eliminar un autor con libros asociados.")
        instance.delete() # Delete the author if no associated books

# ViewSet for the Libro model
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all() # Get all Libro objects
    serializer_class = LibroSerializer # Use LibroSerializer for serialization