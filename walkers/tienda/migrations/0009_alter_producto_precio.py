# Generated by Django 4.2.2 on 2023-06-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_remove_subcategoria_nombrecategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
