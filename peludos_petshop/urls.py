from django.urls import path
from .views import home, alimentos_secos_perro, alimentos_enlatados_perro

urlpatterns = [
    path('', home, name="home"),
    path('alimentos_secos_perro/', alimentos_secos_perro, name="alimentos_secos_perro"),
    path('alimentos_enlatados_perro/', alimentos_enlatados_perro, name="alimentos_enlatados_perro"),
]