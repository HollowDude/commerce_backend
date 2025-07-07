from django.db import models
from .orden import Orden
from .producto import Producto

class Orden_Producto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='orden_productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='orden_productos')
    cantidad = models.IntegerField()