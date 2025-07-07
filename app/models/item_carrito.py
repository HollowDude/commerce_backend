from django.db import models
from .producto import Producto
from .carrito import Carrito

'''Al final no use esto pero si gestionase como debe ser los pedidos es necesario'''

class ItemCarrito(models.Model):
    carrito   = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    product   = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='carrito_items')
    cantidad  = models.IntegerField()