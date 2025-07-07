from django.db import models
from .usuario import Usuario

class Carrito(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrito')