# Generated by Django 4.2.2 on 2023-06-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_remove_producto_categoria_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ManyToManyField(to='tienda.producto'),
        ),
    ]