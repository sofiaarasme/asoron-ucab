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


class PersonaContacto(models.Model):
    contacto_id = models.AutoField(primary_key=True)
    contacto_nombre = models.CharField(max_length=50)
    contacto_apellido = models.CharField(max_length=50)
    contacto_cargo = models.CharField(max_length=50)
    # fk_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='fk_proveedor', blank=True, null=True)
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True, related_name='contactos')

    class Meta:
        managed = False
        db_table = 'persona_contacto'


class Telefono(models.Model):
    telefono_id = models.AutoField(primary_key=True)
    telefono_codigo = models.CharField(max_length=50)
    telefono_numero = models.CharField(max_length=50)
    fk_persona_contacto = models.ForeignKey(PersonaContacto, models.DO_NOTHING, db_column='fk_persona_contacto', blank=True, null=True, related_name='telefonos')
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='fk_empleado', blank=True, null=True, related_name='telefonos')
    fk_natural = models.ForeignKey(Cliente_natural, models.DO_NOTHING, db_column='fk_natural', blank=True, null=True, related_name='telefonos')
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True, related_name='telefonos')
    # fk_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='fk_proveedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefono'


class Correo(models.Model):
    correo_id = models.AutoField(primary_key=True)
    correo_direccion = models.CharField(unique=True, max_length=50)
    # fk_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='fk_proveedor', blank=True, null=True)
    fk_natural = models.ForeignKey(Cliente_natural, models.DO_NOTHING, db_column='fk_natural', blank=True, null=True, related_name='correos')
    fk_juridico = models.ForeignKey(Cliente_juridico, models.DO_NOTHING, db_column='fk_juridico', blank=True, null=True, related_name='correos')
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='fk_empleado', blank=True, null=True, related_name='correos')

    class Meta:
        managed = False
        db_table = 'correo'
