from django.http import Http404
from django.shortcuts import render, redirect
from .models import Producto, TipoMascota, TipoProducto
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, 'peludos_petshop/menu_principal.html')

def home_admin(request):

    return render(request, 'peludos_petshop/Vista_admin/home_admin.html')

def listar_productos_perro(request):
    producto = Producto.objects.all().order_by('nomProducto')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(producto, 9)
        producto = paginator.page(page)
    except:
        raise Http404

    contexto = {
        "entity": producto,
        "paginator": paginator
    }

    return render(request, 'peludos_petshop/Vista_admin/listar_productos_perros.html', contexto)


def listar_mascota_productos(request):
    tipo_mascota = TipoMascota.objects.all()
    tipo_producto = TipoProducto.objects.all()
    contexto = {
        "tipo_m": tipo_mascota,
        "tipo_p": tipo_producto
    }

    return render(request, 'peludos_petshop/Vista_admin/agregar_productos.html', contexto)

def registar_producto(request):
    id_producto = request.POST['id_producto']
    nombre_p = request.POST['nombre']
    precio_p = request.POST['precio']
    stock_p = request.POST['stock']
    descripcion_p = request.POST['descripcion']
    img_foto = request.FILES['foto_m']
    tipo_m = request.POST['tip_mascota']
    tipo_p = request.POST['tip_producto']
    #obtener el registro completo de la mascota y tipo producto
    mascota_c = TipoMascota.objects.get(idMascota = tipo_m)
    tipo_producto_c = TipoProducto.objects.get(idTipoProducto = tipo_p)

    #insert
    Producto.objects.create(idProducto =id_producto, nomProducto = nombre_p, precio = precio_p, stock = stock_p, descripcion = descripcion_p, fotoProducto = img_foto, tipoMascota = mascota_c, tipoProducto = tipo_producto_c) 

    messages.success(request,'Producto Registrada')

    return redirect('agregar_productos')

def eliminar_producto(request, id):
    producto1 = Producto.objects.get(idProducto = id)
    producto1.delete() #elimina el registro
    messages.success(request,'Producto Eliminada')

    return redirect('listar_productos_perro')

def modificar_productos(request, id):
    producto1 = Producto.objects.get(idProducto = id) # obtengo los datos del producto
    mascota1 = TipoMascota.objects.all() #obtener todos los tipos de mascotas para llenar el combobox
    tipo_p1 = TipoProducto.objects.all() #obtener todos los tipos de productos para llenar el combobox

    contexto = {
        "producto": producto1,
        "mascotas": mascota1,
        "tipo_productos": tipo_p1 
    }

    return render(request,'peludos_petshop/Vista_admin/modificar_productos.html',contexto)

def modificar(request):
    id_producto = request.POST['id_producto']
    nombre_p = request.POST['nombre']
    precio_p = request.POST['precio']
    stock_p = request.POST['stock']
    descripcion_p = request.POST['descripcion']

    producto = Producto.objects.get(idProducto = id_producto) #el registro original
    #comienzo a reemplazar los valores en ese registro original
    producto.nomProducto = nombre_p
    producto.precio = precio_p
    producto.stock = stock_p
    producto.descripcion = descripcion_p

    producto.save() #update

    messages.success(request, 'Producto modificado')

    return redirect('listar_productos_perro')

def alimentos_secos_perro(request):
    productos = Producto.objects.all().order_by('nomProducto')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404

    contexto = {
        "entity": productos,
        "paginator": paginator
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_secos_perro.html',contexto)

def alimentos_enlatados_perro(request):
    productos = Producto.objects.all().order_by('nomProducto')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404

    contexto = {
        "entity": productos,
        "paginator": paginator
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_enlatados_perro.html',contexto)

def detalle_producto(request, id):
    producto = Producto.objects.filter(idProducto = id).first()
    contexto = {"producto": producto}
    return render(request, 'peludos_petshop/Vista_usuario/detalle_producto.html', contexto)



