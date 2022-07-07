from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, TipoMascota, TipoProducto, Contacto
from .forms import ProductoForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def home(request):
    contactos = Contacto.objects.all()
    mascotas = TipoMascota.objects.all().order_by('idMascota')
    contexto = {
        "contacto": contactos,
        "mascotas": mascotas
    }

    return render(request, 'peludos_petshop/menu_principal.html', contexto)

def registrar_contacto(request):
    nombre_contacto = request.POST['nom_contacto']
    correo_contacto = request.POST['email']
    asunto_contacto = request.POST['asunto']
    mensaje_contacto = request.POST['mensaje']

    Contacto.objects.create(nombreContacto = nombre_contacto, correoContacto = correo_contacto, asunto = asunto_contacto, mensajeContacto = mensaje_contacto) 

    messages.success(request,'Contacto enviado correctamente')

    return redirect('home')

@permission_required('peludos_petshop.view_producto')
def home_admin(request):

    return render(request, 'peludos_petshop/Vista_admin/home_admin.html')

def listar_productos(request):
    producto = Producto.objects.all().order_by('nomProducto')
    page1 = request.GET.get('page', 1)

    try:
        paginator = Paginator(producto, 9)
        producto = paginator.page(page1)
    except:
        raise Http404

    contexto = {
        "entity": producto,
        "paginator": paginator
    }

    return render(request, 'peludos_petshop/Vista_admin/listado_productos.html', contexto)

def agregar_productos(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            messages.success(request,'Producto Agregado')
            return redirect('agregar_productos')

        else:
            data["form"] = formulario

    return render(request, 'peludos_petshop/Vista_admin/agregar_productos.html', data)


def eliminar_producto(request, id):
    producto1 = Producto.objects.get(idProducto = id)
    producto1.delete() #elimina el registro
    messages.success(request,'Producto Eliminado')
    return redirect('listar_productos')

def modificar_productos(request, id):

    producto = get_object_or_404(Producto, idProducto = id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto modificado correctamente')
            return redirect('listar_productos')
        data["form"] = formulario

    return render(request,'peludos_petshop/Vista_admin/modificar_productos.html', data)

def lista_contactos(request):
    listado = Contacto.objects.all()
    contexto = {
        "listado": listado  
    }

    return render(request, 'peludos_petshop/vista_admin/listar_contactos.html', contexto)

def eliminar_contacto(request, id_contacto):
    listado1 = Contacto.objects.get(idContacto = id_contacto)
    listado1.delete() 
    messages.success(request,'contacto eliminado')

    return redirect('lista_contactos')

def alimentos_secos_perro(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_secos_perro.html',contexto)

def alimentos_humedos_perro(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_humedos_perro.html',contexto)

def snack_perro(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/snack_perro.html',contexto)

def juguete_perro(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/juguete_perro.html',contexto)

def alimentos_secos_gato(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_secos_gato.html', contexto)

def alimentos_humedos_gato(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_humedos_gato.html', contexto)

def arena_sanitaria_gato(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/arena_sanitaria_gato.html', contexto)

def snack_gato(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/snack_gato.html', contexto)

def juguete_gato(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/juguete_gato.html', contexto)

def alimentos_conejo(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_conejo.html', contexto)

def accesorios_conejo(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/accesorios_conejo.html', contexto)

def alimentos_erizo(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_erizo.html', contexto)

def accesorios_erizo(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/accesorios_erizo.html', contexto)

def alimentos_hamster(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_hamster.html', contexto)

def accesorios_hamster(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/accesorios_hamster.html', contexto)

def alimentos_hurron(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/alimentos_hurron.html', contexto)

def accesorios_hurron(request):
    productos = Producto.objects.all().order_by('nomProducto')

    contexto = {
        "productos": productos
    }

    return render(request, 'peludos_petshop/Vista_usuario/accesorios_hurron.html', contexto)

def detalle_producto(request, id):
    producto = Producto.objects.filter(idProducto = id).first()
    contexto = {"producto": producto}

    return render(request, 'peludos_petshop/Vista_usuario/detalle_producto.html', contexto)

def registro_usuario(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            redirect('home')
        
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def carrito_de_compras(request):

    return render(request, 'peludos_petshop/Vista_usuario/carrito.html')