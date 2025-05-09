# Generated by Django 4.2.7 on 2023-12-23 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('venta_num', models.IntegerField(primary_key=True, serialize=False)),
                ('venta_fecha', models.DateField()),
                ('venta_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'venta',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='premio',
            name='FK_evento',
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'managed': False},
        ),
        migrations.DeleteModel(
            name='Entrada',
        ),
        migrations.DeleteModel(
            name='Premio',
        ),
    ]
