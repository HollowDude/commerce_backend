from rest_framework import serializers
from app.serializers.productoSerializer import ProductoSerializer
from ..models import ItemCarrito, Producto

class ItemCarritoSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        write_only=True
        )
    producto = ProductoSerializer(source='product', read_only=True)

    class Meta:
        model = ItemCarrito
        fields = ['id', 'product', 'producto', 'cantidad']