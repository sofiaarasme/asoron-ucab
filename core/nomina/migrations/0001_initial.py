# Generated by Django 4.2.7 on 2023-12-19 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('departamento_id', models.AutoField(primary_key=True, serialize=False)),
                ('departamento_nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('departamento_descripcion', models.TextField(max_length=250, verbose_name='Descripción')),
                ('departamento_gerente', models.CharField(max_length=50, verbose_name='Gerente')),
                ('departamento_num_empleados', models.IntegerField(default=0, verbose_name='Número de empleados')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'Departamento',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('tienda_id', models.AutoField(primary_key=True, serialize=False)),
                ('tienda_razon_social', models.CharField(max_length=50, verbose_name='Razón Social')),
                ('tienda_descripcion', models.TextField(max_length=250, verbose_name='Descripción')),
                ('tienda_pag_web', models.CharField(max_length=50, verbose_name='Página Web')),
                ('tienda_direccion', models.CharField(max_length=250, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
                'db_table': 'Tienda',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleado_id', models.AutoField(primary_key=True, serialize=False)),
                ('empleado_ci', models.CharField(max_length=8, unique=True, verbose_name='Cédula')),
                ('empleado_primer_nombre', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('empleado_segundo_nombre', models.CharField(max_length=50, verbose_name='Segundo Nombre')),
                ('empleado_primer_apellido', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('empleado_segundo_apellido', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('empleado_sueldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Sueldo')),
                ('empleado_cargo', models.CharField(max_length=80, verbose_name='Cargo')),
                ('FK_Departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.departamento', verbose_name='Departamento')),
                ('FK_Tienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nomina.tienda', verbose_name='Tienda')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
            },
        ),
    ]
