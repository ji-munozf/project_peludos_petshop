from django.urls import path
from .views import home, alimentos_secos_perro, alimentos_enlatados_perro, detalle_producto

urlpatterns = [
    path('', home, name="home"),
    path('alimentos_secos_perro/', alimentos_secos_perro, name="alimentos_secos_perro"),
    path('alimentos_enlatados_perro/', alimentos_enlatados_perro, name="alimentos_enlatados_perro"),
    path('detalle_producto/<str:id>', detalle_producto, name="detalle_producto"),
]