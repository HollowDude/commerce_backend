from django.db import models
from .usuario import Usuario

CATS=[
    ('Comida','Comida'),
    ('Hogar', 'Hogar'),
    ('Electronicos', 'Electronicos'),
    ('Herramientas', 'Herramientas')
]

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField()
    categoria = models.CharField(choices=CATS)
    precio_general = models.FloatField(null=True, blank = True)
    publicado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='productos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre