from rest_framework import serializers
from peludos_petshop.models import Producto, TipoMascota, TipoProducto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class IdMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMascota
        fields = '__all__'

class IdTipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'