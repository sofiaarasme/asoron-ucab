# Generated by Django 4.2.7 on 2023-12-19 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nomina', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('telefono_id', models.AutoField(primary_key=True, serialize=False)),
                ('telefono_tipo', models.CharField(max_length=50, verbose_name='Tipo de teléfono')),
                ('telefono_numero', models.CharField(max_length=11, verbose_name='Número de teléfono')),
                ('FK_empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefonos', to='nomina.empleado')),
                ('FK_juridico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente_juridico')),
                ('FK_natural', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente_natural')),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
                'db_table': 'Telefono',
            },
        ),
    ]
