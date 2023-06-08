# Generated by Django 4.2.2 on 2023-06-07 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_subcategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategoria',
            name='categoria',
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria'),
        ),
    ]