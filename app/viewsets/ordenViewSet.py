from django.forms import ValidationError
from rest_framework import viewsets, permissions
from django.db import transaction
from app.models.carrito import Carrito
from app.models.orden_producto import Orden_Producto
from app.models.producto import Producto
from ..models import Orden
from ..serializers.ordenSerializer import OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all().select_related('user')
    serializer_class = OrdenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Orden.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        1. Crea la Orden.
        2. Por cada ItemCarrito:  
          - Verifica stock, lo reduce.  
          - Crea Orden_Producto.  
          - Borra el ItemCarrito.  
        """
        user_perfil = self.request.user.usuario

        try:
            carrito = Carrito.objects.get(user=user_perfil)
        except Carrito.DoesNotExist:
            carrito = None

        items = carrito.items.select_related('product') if carrito else []

        if not items:
            raise ValidationError("El carrito está vacío.")

        with transaction.atomic():
            orden = serializer.save(user=user_perfil)

            for item in items:
                prod: Producto = item.product
                if prod.stock < item.cantidad:
                    raise ValidationError(
                        f"Stock insuficiente para el producto {prod.nombre}."
                    )
                prod.stock -= item.cantidad
                prod.save(update_fields=['stock'])

                Orden_Producto.objects.create(
                    orden=orden,
                    producto=prod,
                    cantidad=item.cantidad
                )

            items.delete()
