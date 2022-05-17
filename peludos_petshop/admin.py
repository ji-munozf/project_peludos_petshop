from django.contrib import admin
from .models import TipoMascota, TipoProducto, Producto

# Register your models here.

admin.site.register(TipoMascota)
admin.site.register(TipoProducto)
admin.site.register(Producto)