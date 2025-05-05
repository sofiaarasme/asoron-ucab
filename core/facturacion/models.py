# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from core.clientes.models import Cliente_natural, Cliente_juridico


class Punto(models.Model):
    punto_id = models.AutoField(primary_key=True)
    punto_valor = models.DecimalField(max_digits=10, decimal_places=2)
    punto_fecha_inicio = models.DateField()
    punto_fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'punto'


class Conversion_divisa(models.Model):
    cd_id = models.AutoField(primary_key=True)
    cd_valor = models.DecimalField(max_digits=10, decimal_places=2)
    cd_fecha_inicio = models.DateField()
    cd_fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'conversion_divisa'


class Tarjeta(models.Model):
    metodo_pago_id = models.AutoField(primary_key=True)
    tarjeta_numero = models.CharField(max_length=50)
    tarjeta_banco = models.CharField(max_length=50)
    tarjeta_cvv = models.IntegerField()
    tarjeta_fecha_vencimiento = models.DateField()
    fk_natural = models.ForeignKey(Cliente_natural, models.DO_NOTHING, db_column='fk_natural', blank=True, null=True, related_name='tarjetas_natural')
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True, related_name='tarjetas_juridico')

    class Meta:
        managed = False
        db_table = 'tarjeta'


class PuntoMetodo(models.Model):
    metodo_pago_id = models.AutoField(primary_key=True)
    punto_metodo_cantidad = models.IntegerField()
    fk_natural = models.ForeignKey(Cliente_natural, models.DO_NOTHING, db_column='fk_natural', blank=True, null=True)
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'punto_metodo'


class Efectivo(models.Model):
    metodo_pago_id = models.AutoField(primary_key=True)
    efectivo_denominacion = models.IntegerField()
    fk_natural = models.ForeignKey(Cliente_natural, models.DO_NOTHING, db_column='fk_natural', blank=True, null=True)
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'efectivo'


class Cheque(models.Model):
    metodo_pago_id = models.AutoField(primary_key=True)
    cheque_numero = models.IntegerField()
    cheque_banco = models.CharField(max_length=50)
    fk_natural = models.ForeignKey(Cliente_natural, models.DO_NOTHING, db_column='fk_natural', blank=True, null=True)
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheque'
