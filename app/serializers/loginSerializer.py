from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        try:
            perfil = self.user.usuario
            rol = perfil.rol
            metodos = perfil.metodos
        except Exception:
            perfil = None
            rol = None
            metodos = None

        data['user'] = {
            'id':       self.user.id,
            'username': self.user.username,
            'email':    self.user.email,
            'rol': {
                'id':       rol.id if rol else None,
                'rol_name': rol.rol_name if rol else None,
            },
            'metodos':  metodos,
        }
        return data