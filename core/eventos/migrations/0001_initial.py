# Generated by Django 4.2.7 on 2023-12-19 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('evento_id', models.AutoField(primary_key=True, serialize=False)),
                ('evento_nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('evento_fecha_inicio', models.DateField()),
                ('evento_fecha_fin', models.DateField()),
                ('evento_ubicacion', models.CharField(max_length=255, verbose_name='Ubicacion')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'db_table': 'Evento',
            },
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('premio_id', models.AutoField(primary_key=True, serialize=False)),
                ('premio_nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('premio_descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('FK_evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
            options={
                'verbose_name': 'Premio',
                'verbose_name_plural': 'Premios',
                'db_table': 'Premio',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('entrada_id', models.AutoField(primary_key=True, serialize=False)),
                ('entrada_fecha', models.DateTimeField()),
                ('entrada_descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('FK_evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'db_table': 'Entrada',
            },
        ),
    ]
