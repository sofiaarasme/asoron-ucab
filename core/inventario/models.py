# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from core.nomina.models import *
from core.compras.models import *


class MateriaPrima(models.Model):
    materia_prima_id = models.AutoField(primary_key=True)
    materia_prima_nombre = models.CharField(max_length=50)
    materia_prima_tipo = models.CharField(max_length=50)
    materia_prima_descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.materia_prima_nombre

    class Meta:
        managed = False
        db_table = 'materia_prima'


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_nombre = models.CharField(max_length=50)
    color_descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.color_nombre

    class Meta:
        managed = False
        db_table = 'color'

class Tapa(models.Model):
    tapa_id = models.AutoField(primary_key=True)
    tapa_nombre = models.CharField(max_length=50)
    tapa_descripcion = models.CharField(max_length=150)
    fk_materia_prima = models.ForeignKey(MateriaPrima, models.DO_NOTHING, db_column='fk_materia_prima')
    fk_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='fk_color')

    def __str__(self):
        return self.tapa_nombre

    class Meta:
        managed = False
        db_table = 'tapa'


class Ron(models.Model):
    ron_id = models.AutoField(primary_key=True)
    ron_nombre = models.CharField(max_length=50)
    ron_descripcion = models.CharField(max_length=150)
    fk_lugar = models.ForeignKey(Lugar, models.DO_NOTHING, db_column='fk_lugar')
    # fk_barril = models.ForeignKey('barril', models.DO_NOTHING, db_column='fk_barril')
    # fk_tipo_ron = models.ForeignKey('tipo_ron', models.DO_NOTHING, db_column='fk_tipo_ron')
    # fk_mezcla = models.ForeignKey('mezcla', models.DO_NOTHING, db_column='fk_mezcla')

    def __str__(self):
        return self.ron_nombre

    class Meta:
        managed = False
        db_table = 'ron'


class Botella(models.Model):
    botella_id = models.AutoField(primary_key=True)
    botella_nombre = models.CharField(max_length=50)
    botella_precio = models.DecimalField(max_digits=10, decimal_places=2)
    botella_capacidad = models.DecimalField(max_digits=10, decimal_places=2)
    botella_ancho = models.DecimalField(max_digits=10, decimal_places=2)
    botella_alto = models.DecimalField(max_digits=10, decimal_places=2)
    fk_ron = models.ForeignKey(Ron, models.DO_NOTHING, db_column='fk_ron')
    fk_tapa = models.ForeignKey(Tapa, models.DO_NOTHING, db_column='fk_tapa')
    fk_materia_prima = models.ForeignKey(MateriaPrima, models.DO_NOTHING, db_column='fk_materia_prima')
    fk_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='fk_proveedor', blank=True, null=True)

    def __str__(self):
        return self.botella_nombre

    class Meta: 
        managed = False
        db_table = 'botella'


class Inventario(models.Model):
    inventario_id = models.AutoField(primary_key=True)
    inventario_descripcion = models.CharField(max_length=150)
    inventario_cantidad = models.IntegerField()
    fk_botella = models.ForeignKey(Botella, models.DO_NOTHING, db_column='fk_botella')
    fk_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='fk_departamento')

    def __str__(self):
        return self.inventario_descripcion

    class Meta:
        managed = False
        db_table = 'inventario'
