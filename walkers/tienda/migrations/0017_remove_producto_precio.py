# Generated by Django 4.2.2 on 2023-06-07 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0016_delete_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
    ]
