from rest_framework import viewsets, permissions
from rest_framework.response import Response
from ..models import Carrito, ItemCarrito
from ..serializers import CarritoSerializer, ItemCarritoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        carrito, _ = Carrito.objects.get_or_create(user=self.request.user.usuario)
        return carrito

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.usuario)

    def list(self, request, *args, **kwargs):
        carrito = self.get_object()
        serializer = self.get_serializer(carrito)
        return Response(serializer.data)