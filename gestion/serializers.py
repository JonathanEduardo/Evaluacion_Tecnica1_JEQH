# SETTINS ENDPOINTS API g m
from rest_framework import serializers
from .models import Autor, Libro

#Serializacion  poara el modelo Autor
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor 
        fields = '__all__' #incluimos todos los campos del modelo establecido

#Serializacion  poara el modelo Libro
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__' #incluimos todos los campos del modelo establecido
