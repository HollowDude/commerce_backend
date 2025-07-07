from rest_framework import viewsets, permissions
from ..models import Rol
from ..serializers.rolSerializer import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permissions.IsAdminUser]
