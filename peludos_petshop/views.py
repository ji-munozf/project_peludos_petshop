from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    contexto = {"producto": productos}
    return render(request, 'peludos_petshop/menu_principal.html', contexto)

def alimentos_secos_perro(request):
    productos = Producto.objects.all()
    contexto = {"producto": productos}
    return render(request, 'peludos_petshop/Vista_usuario/alimentos_secos_perro.html',contexto)

def alimentos_enlatados_perro(request):
    productos = Producto.objects.all()
    contexto = {"producto": productos}
    return render(request, 'peludos_petshop/Vista_usuario/alimentos_enlatados_perro.html',contexto)

def detalle_producto(request, id):
    producto = Producto.objects.filter(idProducto = id).first()
    contexto = {"producto": producto}
    return render(request, 'peludos_petshop/Vista_usuario/detalle_producto.html', contexto)