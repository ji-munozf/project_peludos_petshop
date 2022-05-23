from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):

    return render(request, 'peludos_petshop/menu_principal.html')

def alimentos_secos_perro(request):
    productos = Producto.objects.all()
    contexto = {"producto": productos}
    return render(request, 'peludos_petshop/alimentos_secos_perro.html',contexto)