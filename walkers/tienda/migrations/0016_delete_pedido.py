# Generated by Django 4.2.2 on 2023-06-07 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0015_alter_pedido_precio_alter_producto_precio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]