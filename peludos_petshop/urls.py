from django.urls import path
from .views import home, alimentos_secos_perro, alimentos_enlatados_perro, detalle_producto, home_admin, listar_productos_perro

urlpatterns = [
    path('', home, name="home"),
    path('home_admin/', home_admin, name="home_admin"),
    path('alimentos_secos_perro/', alimentos_secos_perro, name="alimentos_secos_perro"),
    path('alimentos_enlatados_perro/', alimentos_enlatados_perro, name="alimentos_enlatados_perro"),
    path('detalle_producto/<str:id>', detalle_producto, name="detalle_producto"),
    path('listar_productos_perro/', listar_productos_perro, name="listar_productos_perro"),
]