from django.db import models
from .cliente import Cliente
from .item import Item


class Factura(models.Model):
    id_factura = models.BigAutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_usuario = models.CharField(max_length = 50, unique=True)
    id_sucursal = models.CharField(max_length = 50, unique=True)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)
    costo_total = models.IntegerField(null=True, blank=True)
    
                  