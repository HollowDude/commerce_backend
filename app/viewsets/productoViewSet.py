from rest_framework import viewsets, permissions
from ..permissions.permissions import IsVendedor
from ..models import Producto, Orden_Producto
from rest_framework.decorators import action
from django.db.models import Sum
from rest_framework.response import Response
from ..serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsVendedor()]
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(publicado_por=self.request.user.usuario)

    def get_queryset(self):
        if self.action == 'list' and 'mis_productos' in self.request.query_params:
            return Producto.objects.filter(publicado_por=self.request.user.usuario)
        return super().get_queryset()
    
    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        usuario = request.user.usuario

        total_productos = Producto.objects.filter(publicado_por=usuario).count()
        productos_agotados = Producto.objects.filter(
            publicado_por=usuario,
            stock=0
        ).count()

        ventas = Orden_Producto.objects.filter(
            producto__publicado_por=usuario
        ).aggregate(
            total_ventas=Sum('cantidad'),
            ingresos_totales=Sum('cantidad') * Sum('producto__precio')
        )

        data = {
            'totalProductos': total_productos,
            'totalVentas': ventas['total_ventas'] or 0,
            'ingresosTotales': float(ventas['ingresos_totales'] or 0) if ventas['ingresos_totales'] else 0,
            'productosAgotados': productos_agotados
        }

        return Response(data)