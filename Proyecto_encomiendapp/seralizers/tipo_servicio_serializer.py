from rest_framework.fields import Field
from Proyecto_encomiendapp import models
from models import tipo_servicio
from rest_framework import serializers

class TipoServicioSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.tipo_servicio
        fields = ('id_servicio', 'tipo_servicio','descripcion','costo_servicio',
        'peso_maximo','volumen_maximo','peso_adicional','volumen_adicional')
 
     
     