from rest_framework.permissions import BasePermission, SAFE_METHODS

from app.models.usuario import Usuario

class AllowAnyCreate(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.method in ['POST', 'PUT', 'PATCH']:
            print("pahm")
            return True
        return request.user and request.user.is_authenticated


class IsVendedor(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        print(hasattr(request.user, 'rol'))
        if not request.user or not request.user.is_authenticated:
            return False
        try:
            usuario = request.user.usuario 
            return usuario.rol.id == 2
        except (Usuario.DoesNotExist, AttributeError):
            return False
