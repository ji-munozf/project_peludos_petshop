from rest_framework import serializers
from peludos_petshop.models import Producto, TipoMascota, TipoProducto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TipoMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMascota
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'