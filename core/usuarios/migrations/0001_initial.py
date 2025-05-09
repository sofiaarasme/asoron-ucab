# Generated by Django 4.2.7 on 2024-01-18 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nomina', '0003_beneficio_beneficioempleado_horario_horarioempleado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('permiso_id', models.AutoField(primary_key=True, serialize=False)),
                ('permiso_nombre', models.CharField(max_length=50)),
                ('permiso_tipo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'permiso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_nombre', models.CharField(max_length=50)),
                ('rol_descripcion', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_nombre', models.CharField(max_length=50, unique=True)),
                ('usuario_contrasena', models.CharField(max_length=50)),
                ('fk_empleado', models.ForeignKey(db_column='fk_empleado', on_delete=django.db.models.deletion.DO_NOTHING, to='nomina.empleado')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RolPermiso',
            fields=[
                ('fk_rol', models.OneToOneField(db_column='fk_rol', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='usuarios.rol')),
            ],
            options={
                'db_table': 'rol_permiso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioRol',
            fields=[
                ('fk_usuario', models.OneToOneField(db_column='fk_usuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuario_rol',
                'managed': False,
            },
        ),
    ]
