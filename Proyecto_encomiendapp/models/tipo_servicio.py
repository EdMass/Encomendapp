from django.db import models

class TipoServicio(models.Model):
    id_servicio = models.CharField(max_length = 5, unique=True)
    tipo_servicio = models.CharField(max_length = 15, unique=True)
    descripcion = models.CharField(max_length = 100, unique=True)
    costo_servicio = models.IntegerField(null=True, blank=True)
    peso_maximo = models.FloatField()
    volumen_maximo = models.FloatField()
    peso_adicional = models.FloatField()
    volumen_adicional = models.FloatField()
    
    
    
    