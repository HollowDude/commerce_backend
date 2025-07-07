from django.db import models
from django.contrib.auth.models import User
from .rol import Rol

METODOS = [
    ('Transfermovil','Transfermovil'),
    ('Enzona', 'Enzona')
]

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    metodos = models.CharField(choices=METODOS, max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, related_name="users")