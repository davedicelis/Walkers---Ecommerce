# Generated by Django 4.2.2 on 2023-06-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0013_alter_pedido_precio_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]