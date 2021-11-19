from Proyecto_encomiendapp import models
from models import factura 
from rest_framework import serializers

class FacturaSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.factura
        fields = ('id_factura', 'id_cliente','id_usuario','id_sucursal',
        'id_item','fecha','costo_total')
 
  