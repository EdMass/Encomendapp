from django.db import models
from models import cliente 
from rest_framework import serializers
from Proyecto_encomiendapp import models

class ClienteSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.cliente
        fields = ('id_cliente','nombre','apellido','correo','telefono',
        'id_item','tipo_documento','numero_documento','direccion','genero')

         