# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# from core.facturacion.models import Punto


class Lugar(models.Model):
    lugar_id = models.AutoField(primary_key=True)
    lugar_nombre = models.CharField(max_length=50)
    lugar_tipo = models.CharField(max_length=50)
    fk_lugar = models.ForeignKey('self', models.DO_NOTHING, db_column='fk_lugar', blank=True, null=True)
    
    def __str__(self):
        return self.lugar_nombre

    class Meta:
        managed = False
        db_table = 'lugar'


class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True)
    departamento_nombre = models.CharField(max_length=50)
    departamento_descripcion = models.CharField(max_length=150)
    departamento_gerente = models.CharField(max_length=50)
    departamento_num_empleados = models.IntegerField()

    def __str__(self):
        return self.departamento_nombre

    class Meta:
        managed = False
        db_table = 'departamento'


class Tienda(models.Model):
    tienda_id = models.AutoField(primary_key=True)
    tienda_razon_social = models.CharField(max_length=50)
    tienda_descripcion = models.CharField(max_length=150)
    tienda_pag_web = models.CharField(max_length=50)
    tienda_direccion = models.CharField(max_length=50)
    fk_lugar = models.ForeignKey(Lugar, models.DO_NOTHING, db_column='fk_lugar')
    # fk_punto = models.ForeignKey(Punto, models.DO_NOTHING, db_column='fk_punto')

    def __str__(self):
        return self.tienda_razon_social

    class Meta:
        managed = False
        db_table = 'tienda'


class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    empleado_ci = models.IntegerField(unique=True)
    empleado_primer_nombre = models.CharField(max_length=50)
    empleado_segundo_nombre = models.CharField(max_length=50)
    empleado_primer_apellido = models.CharField(max_length=50)
    empleado_segundo_apellido = models.CharField(max_length=50)
    empleado_sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    empleado_cargo = models.CharField(max_length=50)
    fk_empleado = models.ForeignKey('self', models.DO_NOTHING, db_column='fk_empleado', blank=True, null=True)
    fk_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='fk_departamento')
    fk_tienda = models.ForeignKey(Tienda, models.DO_NOTHING, db_column='fk_tienda')

    def __str__(self):
        return self.empleado_primer_nombre + " " + self.empleado_primer_apellido

    class Meta:
        managed = False
        db_table = 'empleado'

class Horario(models.Model):
    horario_id = models.AutoField(primary_key=True)
    horario_entrada = models.TimeField()
    horario_salida = models.TimeField()
    horario_dia = models.CharField(max_length=50)
    tienen = models.ManyToManyField(Empleado, through= 'HorarioEmpleado')

    def __str__(self):
        return self.horario_dia

    class Meta:
        managed = False
        db_table = 'horario'

class HorarioEmpleado(models.Model):
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='fk_empleado')
    fk_horario = models.ForeignKey(Horario, models.DO_NOTHING, db_column='fk_horario')

    class Meta:
        managed = False
        db_table = 'horario_empleado'

class Beneficio(models.Model):
    beneficio_id = models.AutoField(primary_key=True)
    beneficio_nombre = models.CharField(max_length=50)
    beneficio_descripcion = models.CharField(max_length=150)
    tienen = models.ManyToManyField(Empleado, through= 'BeneficioEmpleado')

    def __str__(self):
        return self.beneficio_nombre

    class Meta:
        managed = False
        db_table = 'beneficio'

class BeneficioEmpleado(models.Model):
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='fk_empleado')
    fk_beneficio = models.ForeignKey(Beneficio, models.DO_NOTHING, db_column='fk_beneficio')

    class Meta:
        managed = False
        db_table = 'beneficio_empleado'
