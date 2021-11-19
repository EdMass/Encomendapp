from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 50, unique=True)
    apellido = models.CharField(max_length = 50, unique=True)
    correo = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length = 25, unique=True)
    tipo_documento = models.CharField(max_length = 30, unique=True)
    numero_documento = models.CharField(max_length = 30, unique=True)
    direccion = models.CharField(max_length = 60, unique=True)
    genero = models.CharField(max_length = 20, unique=True)
    
