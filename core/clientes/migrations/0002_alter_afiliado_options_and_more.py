# Generated by Django 4.2.7 on 2023-12-23 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='afiliado',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='cliente_juridico',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='cliente_natural',
            options={'managed': False},
        ),
    ]
