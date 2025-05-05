# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from core.nomina.models import Empleado

class Permiso(models.Model):
    permiso_id = models.AutoField(primary_key=True)
    permiso_nombre = models.CharField(max_length=50)
    permiso_tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.permiso_nombre} - {self.permiso_tipo}"

    class Meta:
        managed = False
        db_table = 'permiso'


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=50)
    rol_descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'rol'


class RolPermiso(models.Model):
    fk_rol = models.OneToOneField(Rol, models.DO_NOTHING, db_column='fk_rol', primary_key=True)  # The composite primary key (fk_rol, fk_permiso) found, that is not supported. The first column is selected.
    fk_permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='fk_permiso')

    class Meta:
        managed = False
        db_table = 'rol_permiso'
        unique_together = (('fk_rol', 'fk_permiso'),)


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    usuario_nombre = models.CharField(unique=True, max_length=50)
    usuario_contrasena = models.CharField(max_length=50)
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='fk_empleado')

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioRol(models.Model):
    fk_usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='fk_usuario', primary_key=True)  # The composite primary key (fk_usuario, fk_rol) found, that is not supported. The first column is selected.
    fk_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_rol')

    class Meta:
        managed = False
        db_table = 'usuario_rol'
        unique_together = (('fk_usuario', 'fk_rol'),)
