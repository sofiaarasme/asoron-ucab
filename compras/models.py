
from django.db import models
from core.clientes.models import *


class Proveedor(models.Model):
    proveedor_id = models.AutoField(primary_key=True)
    proveedor_razon_social = models.CharField(max_length=50)
    proveedor_den_comercial = models.CharField(max_length=100)
    proveedor_rif = models.CharField(max_length=50)
    proveedor_dir_fisica = models.CharField(max_length=100)
    proveedor_dir_fiscal = models.CharField(max_length=100)

    def __str__(self):
        return self.proveedor_razon_social

    class Meta:
        managed = False
        db_table = 'proveedor'

    
