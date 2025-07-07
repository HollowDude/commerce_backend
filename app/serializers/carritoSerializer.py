from rest_framework import serializers
from ..models import Carrito
from .item_carritoSerializer import ItemCarritoSerializer
''''''


class CarritoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    items = ItemCarritoSerializer(many=True, read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'user', 'items']