# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from core.nomina.models import Lugar
from core.nomina.models import Tienda


class Afiliado(models.Model):
    afiliado_id = models.AutoField(primary_key=True)
    afiliado_fecha_afiliacion = models.DateField()
    afiliado_numero_carnet = models.IntegerField(unique=True)
    afiliado_codigo_qr = models.CharField(unique=True, max_length=50)
    fk_tienda = models.ForeignKey(Tienda, models.DO_NOTHING, db_column='fk_tienda')

    class Meta:
        managed = False
        db_table = 'afiliado'


class Cliente_natural(models.Model):
    cliente_n_rif = models.IntegerField(primary_key=True)
    cliente_cantidad_puntos = models.IntegerField(blank=True, null=True)
    cliente_cedula = models.IntegerField(unique=True)
    cliente_p_nombre = models.CharField(max_length=50)
    cliente_s_nombre = models.CharField(max_length=50)
    cliente_p_apellido = models.CharField(max_length=50)
    cliente_s_apellido = models.CharField(max_length=50)
    cliente_direccion = models.CharField(max_length=50)
    fk_lugar = models.ForeignKey(Lugar, models.DO_NOTHING, db_column='fk_lugar')

    class Meta:
        managed = False
        db_table = 'cliente_natural'


class Cliente_juridico(models.Model):
    cliente_j_rif = models.IntegerField(primary_key=True)
    cliente_cantidad_puntos = models.IntegerField(blank=True, null=True)
    cliente_denominacion_comercial = models.CharField(max_length=100)
    cliente_razon_social = models.CharField(max_length=50)
    cliente_pagina_web = models.CharField(max_length=50)
    cliente_capital_disponible = models.IntegerField()
    cliente_direccion_fiscal = models.CharField(max_length=50)
    cliente_direccion_fisica = models.CharField(max_length=50)
    fk_lugar = models.ForeignKey(Lugar, models.DO_NOTHING, db_column='fk_lugar')

    class Meta:
        managed = False
        db_table = 'cliente_juridico'
