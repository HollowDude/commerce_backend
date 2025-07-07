from rest_framework import serializers
from django.conf import settings
from ..models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'rol_name']