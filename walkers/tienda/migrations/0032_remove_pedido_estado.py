# Generated by Django 4.2.2 on 2023-06-08 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0031_remove_pedido_producto_pedido_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
    ]