from rest_framework import serializers
from ..models import Orden
from .orden_productoSerializer import OrdenProductoSerializer

class OrdenSerializer(serializers.ModelSerializer):
    orden_productos = OrdenProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = ['id', 'user', 'total', 'created_at', 'orden_productos']
        read_only_fields = ['user', 'created_at']
