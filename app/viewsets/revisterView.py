from rest_framework import generics, permissions
from ..serializers.registerSerializer import RegisterSerializer
from ..models import Usuario

class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
