# Generated by Django 4.0.4 on 2022-05-25 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peludos_petshop', '0003_remove_producto_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoproducto',
            old_name='idMascota',
            new_name='idProducto',
        ),
    ]