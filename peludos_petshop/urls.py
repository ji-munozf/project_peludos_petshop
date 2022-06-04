from django.urls import path
from .views import home, alimentos_secos_perro, alimentos_enlatados_perro, detalle_producto, home_admin, listar_productos_perro, listar_mascota_productos, registar_producto, eliminar_producto, modificar_productos, modificar
urlpatterns = [
    path('', home, name="home"),
    path('home_admin/', home_admin, name="home_admin"),
    path('alimentos_secos_perro/', alimentos_secos_perro, name="alimentos_secos_perro"),
    path('alimentos_enlatados_perro/', alimentos_enlatados_perro, name="alimentos_enlatados_perro"),
    path('detalle_producto/<str:id>', detalle_producto, name="detalle_producto"),
    path('listar_productos_perro', listar_productos_perro, name="listar_productos_perro"),
    path('agregar_productos', listar_mascota_productos, name="agregar_productos"),
    path('registro', registar_producto, name="registro"),
    path('eliminar/<int:id>',eliminar_producto, name="eliminar_producto"),
    path('modificar_productos/<int:id>', modificar_productos, name="modificar_productos"),
    path('modificar', modificar, name="modificar"),
]