# Generated by Django 4.2.2 on 2023-06-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0037_pedido_cantidad_pedido_direccion_pedido_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='producto',
            field=models.ManyToManyField(to='tienda.producto'),
        ),
    ]