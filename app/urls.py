from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import usuarioViewSet, productoViewSet, item_carritoViewSet, \
carritoViewSet, ordenViewSet, orden_productoViewSet, rolViewSet, RegisterView, \
LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

router.register('usuario', usuarioViewSet.UsuarioViewSet)
router.register('rol', rolViewSet.RolViewSet)
router.register('producto', productoViewSet.ProductoViewSet)
router.register('carrito', carritoViewSet.CarritoViewSet, basename='carrito')
router.register('item_carrito', item_carritoViewSet.ItemCarritoViewSet, basename='item_carrito')
router.register('orden', ordenViewSet.OrdenViewSet)
router.register('orden_producto', orden_productoViewSet.OrdenProductoViewSet)

urlpatterns = [
    path('token/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register')
] + router.urls
