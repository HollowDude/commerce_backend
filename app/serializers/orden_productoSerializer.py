from rest_framework import serializers
from ..models import Orden_Producto, Producto

class OrdenProductoSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

    class Meta:
        model = Orden_Producto
        fields = ['id', 'producto', 'cantidad', 'orden']
        extra_kwargs = {
            'orden': {'write_only': True},
        }
