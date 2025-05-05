# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from core.nomina.models import *
from core.clientes.models import *


class Evento(models.Model):
    evento_id = models.AutoField(primary_key=True)
    evento_nombre = models.CharField(max_length=50)
    evento_fecha_inicio = models.DateField()
    evento_fecha_fin = models.DateField()
    evento_ubicacion = models.CharField(max_length=100)
    fk_lugar = models.ForeignKey(Lugar, models.DO_NOTHING, db_column='fk_lugar')

    def __str__(self):
        return self.evento_nombre

    class Meta:
        managed = False
        db_table = 'evento'

class Venta(models.Model):
    venta_num = models.IntegerField(primary_key=True)
    venta_fecha = models.DateField()
    venta_total = models.DecimalField(max_digits=10, decimal_places=2)
    fk_tienda = models.ForeignKey(Tienda, models.DO_NOTHING, db_column='fk_tienda')
    fk_natural = models.ForeignKey(Cliente_natural, models.DO_NOTHING, db_column='fk_natural', blank=True, null=True)
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True)
    fk_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='fk_evento', blank=True, null=True)

    def __str__(self):
        return self.venta_num

    class Meta:
        managed = False
        db_table = 'venta'


class DetalleVenta(models.Model):
    venta_cantidad = models.IntegerField()
    venta_precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fk_venta = models.OneToOneField(Venta, models.DO_NOTHING, db_column='fk_venta', primary_key=True)

    def __str__(self):
        return self.fk_venta

    class Meta:
        managed = False
        db_table = 'detalle_venta'

class Entrada(models.Model):
    entrada_id = models.AutoField(primary_key=True)
    entrada_fecha = models.DateField()
    entrada_descripcion = models.CharField(max_length=150)
    entrada_precio = models.DecimalField(max_digits=10, decimal_places=2)
    fk_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='fk_evento')
    fk_detalle_venta = models.ForeignKey(DetalleVenta, models.DO_NOTHING, db_column='fk_detalle_venta', blank=True, null=True)

    def __str__(self):
        return self.entrada_id

    class Meta:
        managed = False
        db_table = 'entrada'
