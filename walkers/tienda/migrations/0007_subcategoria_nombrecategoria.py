# Generated by Django 4.2.2 on 2023-06-07 14:10

from django.db import migrations, models
import tienda.models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_remove_subcategoria_categoria_subcategoria_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='NombreCategoria',
            field=models.CharField(default=1, max_length=250, verbose_name=tienda.models.Categoria),
        ),
    ]