from django.urls import path
from api_rest.views import lista_productos, agregar_producto, detalle_producto
from api_rest.viewsLogin import login

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login', login, name="login"),
]