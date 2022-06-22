from django.urls import path
from api_rest.views import lista_productos, agregar_producto, control_producto, lista_tipo_mascota, agregar_tipo_mascota, control_tipo_mascota, lista_tipo_productos, agregar_tipo_producto, control_tipo_producto
from api_rest.viewsLogin import login

urlpatterns = [
    #Producto
    path('lista_productos', lista_productos, name="lista_productos"),
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('control_producto/<id>', control_producto, name="control_producto"),
    #TipoMascota
    path('lista_tipo_mascota', lista_tipo_mascota, name="lista_tipo_mascota"),
    path('agregar_tipo_mascota', agregar_tipo_mascota, name="agregar_tipo_mascota"),
    path('control_tipo_mascota/<id>', control_tipo_mascota, name="control_tipo_mascota"),
    #TipoProducto
    path('lista_tipo_productos', lista_tipo_productos, name="lista_tipo_productos"),
    path('agregar_tipo_producto', agregar_tipo_producto, name="agregar_tipo_producto"),
    path('control_tipo_producto/<id>', control_tipo_producto, name="control_tipo_producto"),
    #Login
    path('login', login, name="login"),
]