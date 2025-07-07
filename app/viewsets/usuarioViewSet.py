from rest_framework import viewsets
from ..permissions.permissions import AllowAnyCreate
from ..models import Usuario
from ..serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.select_related('usuario', 'rol').all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAnyCreate]
