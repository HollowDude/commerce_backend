from django.db import models
from .usuario import Usuario

class Orden(models.Model):
    user       = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ordenes')
    total      = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)