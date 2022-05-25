from django.db import models

# Create your models here.

#Modelo tipo_mascota
class TipoMascota(models.Model):
    idMascota = models.AutoField(primary_key=True, verbose_name="ID de mascota")
    nomTipoMascota = models.CharField(max_length=50, verbose_name="Nombre tipo de las mascotas")

    def __str__(self):
        return self.nomTipoMascota

#Modelo tipo_producto
class TipoProducto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="ID tipo de producto")
    nomTipoProducto = models.CharField(max_length=50, verbose_name="Nombre tipo del producto")

    def __str__(self):
        return self.nomTipoProducto

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID del producto")
    nomProducto = models.CharField(max_length=100, verbose_name="Nombre del producto")
    precio = models.IntegerField(verbose_name="Precio del producto", null=False, blank= False)
    stock = models.IntegerField(verbose_name="Stock del producto", null=False, blank= False)
    fotoProducto = models.ImageField(upload_to="producto", null=True)
    tipoMascota = models.ForeignKey(TipoMascota,on_delete= models.CASCADE)
    tipoProducto = models.ForeignKey(TipoProducto,on_delete= models.CASCADE)

    def __str__(self):
        return self.nomProducto
