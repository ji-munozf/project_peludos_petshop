from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductoSerializer, TipoMascotaSerializer, TipoProductoSerializer
from peludos_petshop.models import Producto, TipoMascota, TipoProducto

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt

#Producto
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_producto(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def control_producto(request, id):
    try:
        m = Producto.objects.get(idProducto = id)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(m,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#TipoMascota
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def lista_tipo_mascota(request):
    if request.method == 'GET':
        productos = TipoMascota.objects.all()
        serializer = TipoMascotaSerializer(productos,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_tipo_mascota(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = TipoMascotaSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def control_tipo_mascota(request, id):
    try:
        m = TipoMascota.objects.get(idMascota = id)
    except TipoMascota.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TipoMascotaSerializer(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = TipoMascotaSerializer(m,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#TipoProducto
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def lista_tipo_productos(request):
    if request.method == 'GET':
        productos = TipoProducto.objects.all()
        serializer = TipoProductoSerializer(productos,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregar_tipo_producto(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = TipoProductoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def control_tipo_producto(request, id):
    try:
        m = TipoProducto.objects.get(idTipoProducto = id)
    except TipoProducto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TipoProductoSerializer(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = TipoProductoSerializer(m,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)