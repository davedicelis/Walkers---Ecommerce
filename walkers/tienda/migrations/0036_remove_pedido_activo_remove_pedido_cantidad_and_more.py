# Generated by Django 4.2.2 on 2023-06-08 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0035_remove_pedido_estado_pedido_activo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='telefono',
        ),
    ]
