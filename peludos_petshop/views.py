from django.http import Http404
from django.shortcuts import render
from .models import Producto

from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def home(request):

    return render(request, 'peludos_petshop/menu_principal.html')

def home_admin(request):

    return render(request, 'peludos_petshop/Vista_admin/home_admin.html')

def alimentos_secos_perro(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 6)
        productos = paginator.page(page)
    except:
        raise Http404

    contexto = {
        "entity": productos,
        "paginator": paginator
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_secos_perro.html',contexto)

def alimentos_enlatados_perro(request):
    productos = Producto.objects.all()
    contexto = {"producto": productos}
    return render(request, 'peludos_petshop/Vista_usuario/alimentos_enlatados_perro.html',contexto)

def detalle_producto(request, id):
    producto = Producto.objects.filter(idProducto = id).first()
    contexto = {"producto": producto}
    return render(request, 'peludos_petshop/Vista_usuario/detalle_producto.html', contexto)

