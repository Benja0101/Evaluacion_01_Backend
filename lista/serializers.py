from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Contacto



# Serializer para el modelo Contacto
class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = ["url", "nombre", "email", "telefono", "direccion",]

# Serializer para los usuarios
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

# Serializer para los grupos
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

