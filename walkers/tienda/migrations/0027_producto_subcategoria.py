# Generated by Django 4.2.2 on 2023-06-07 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0026_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.subcategoria'),
        ),
    ]
