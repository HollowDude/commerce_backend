from rest_framework import serializers
from django.conf import settings
from ..models import Usuario, Rol
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    rol  = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all()
    )

    class Meta:
        model = Usuario
        fields = ['id', 'user', 'metodos', 'rol']