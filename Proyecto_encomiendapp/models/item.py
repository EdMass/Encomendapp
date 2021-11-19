from django.db import models
from .tipo_servicio import TipoServicio

class Item(models.Model):
    id_item = models.BigAutoField(primary_key=True)
    id_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    peso_item = models.FloatField()
    volumen_item = models.FloatField()
    costo_servicio = models.IntegerField(null=True, blank=True)
    peso_adicional = models.FloatField()
    valor_peso_adicional = models.IntegerField(null=True, blank=True)
    volumen_adicional = models.FloatField()
    valor_volumen_adicional = models.IntegerField(null=True, blank=True)
    ciudad_origen = models.CharField(max_length = 50, unique=True)
    ciudad_destino = models.CharField(max_length = 50, unique=True)
    
    
