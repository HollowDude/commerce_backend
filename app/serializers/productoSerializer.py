from rest_framework import serializers
from ..models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    publicado_por = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'image_url',
            'categoria',
            'precio_general',
            'publicado_por',
        ]

    def get_publicado_por(self, obj):
        return obj.publicado_por.user.username if obj.publicado_por else None