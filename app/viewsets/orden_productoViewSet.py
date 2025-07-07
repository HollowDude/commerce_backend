from rest_framework import viewsets, permissions
from ..models import Orden_Producto
from ..serializers.orden_productoSerializer import OrdenProductoSerializer 

'''Al final no use esto pero si gestionase como debe ser los pedidos es necesario'''

class OrdenProductoViewSet(viewsets.ModelViewSet):
    queryset = Orden_Producto.objects.all().select_related('orden', 'producto')
    serializer_class = OrdenProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Orden_Producto.objects.filter(orden__user=self.request.user)

    def perform_create(self, serializer):
        # el cliente debe pasar una orden, osea: <id_de_orden_existente>
        # y luego me aseguro de que esa orden le pertenezca
        orden = serializer.validated_data['orden']
        if orden.user != self.request.user:
            raise permissions.exceptions.PermissionDenied("No puedes añadir ítems a una orden que no es tuya.")
        serializer.save()
