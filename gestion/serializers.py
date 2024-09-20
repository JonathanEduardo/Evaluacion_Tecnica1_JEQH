# SETTINS ENDPOINTS API 
from rest_framework import serializers
from .models import Autor, Libro

#Serializer model Autor
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor 
        fields = '__all__' #Include all the fields of the established model

#Serializer model Libro
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__' #Include all the fields of the established model
