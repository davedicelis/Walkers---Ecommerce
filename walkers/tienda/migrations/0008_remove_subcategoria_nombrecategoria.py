# Generated by Django 4.2.2 on 2023-06-07 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_subcategoria_nombrecategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategoria',
            name='NombreCategoria',
        ),
    ]
