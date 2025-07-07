from rest_framework import viewsets, permissions
from ..models import Carrito, ItemCarrito
from ..serializers import ItemCarritoSerializer

class ItemCarritoViewSet(viewsets.ModelViewSet):
    serializer_class = ItemCarritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItemCarrito.objects.filter(carrito__user=self.request.user.usuario)

    def perform_create(self, serializer):
        carrito, _ = Carrito.objects.get_or_create(user=self.request.user.usuario)
        serializer.save(carrito=carrito)