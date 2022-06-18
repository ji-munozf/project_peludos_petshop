from django.urls import path
from api_rest.views import lista_productos, agregar_producto, controlP
from api_rest.viewsLogin import login

urlpatterns = [
    path('lista_productos/', lista_productos, name="lista_productos"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('controlP/<id>', controlP, name="controlP"),
    path('login', login, name="login"),
]