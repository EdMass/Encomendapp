from rest_framework import serializers
from Proyecto_encomiendapp import models
from models import item

class ItemSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.item
        field = ('id_item','id_servicio','peso_item','volumen_item','costo_servicio',
        'peso_adicional','valor_peso_adicional','volumen_adicional',
        'valor_volumen_adicional','ciudad_origen','ciudad_destino')

