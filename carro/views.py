from django.shortcuts import render, redirect
from .carro import Carro
from peludos_petshop.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(idProducto=producto_id)
    carro.agregar(producto=producto)

    return redirect('carrito_de_compras')

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(idProducto=producto_id)
    carro.eliminar(producto=producto)

    return redirect('carrito_de_compras')

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(idProducto=producto_id)
    carro.restar_producto(producto=producto)

    return redirect('carrito_de_compras')

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro

    return redirect('carrito_de_compras')