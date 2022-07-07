# Generated by Django 4.0.4 on 2022-07-07 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de contacto')),
                ('nombreContacto', models.CharField(max_length=100, verbose_name='Nombre de contacto')),
                ('correoContacto', models.EmailField(max_length=254, verbose_name='Correo de contacto')),
                ('asunto', models.CharField(max_length=50, verbose_name='Asunto contacto')),
                ('mensajeContacto', models.TextField(verbose_name='Descripción del producto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('idMascota', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de mascota')),
                ('nomTipoMascota', models.CharField(max_length=50, verbose_name='Nombre tipo de las mascotas')),
                ('fotoMascota', models.ImageField(null=True, upload_to='mascotas')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('idTipoProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID tipo de producto')),
                ('nomTipoProducto', models.CharField(max_length=50, verbose_name='Nombre tipo del producto')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del producto')),
                ('nomProducto', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('precio', models.IntegerField(verbose_name='Precio del producto')),
                ('stock', models.IntegerField(verbose_name='Stock del producto')),
                ('descripcion', models.TextField(verbose_name='Descripción del producto')),
                ('fotoProducto', models.ImageField(null=True, upload_to='producto')),
                ('tipoMascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peludos_petshop.tipomascota')),
                ('tipoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peludos_petshop.tipoproducto')),
            ],
        ),
    ]
