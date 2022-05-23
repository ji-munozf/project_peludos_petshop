from django.urls import path
from .views import home, alimentos_secos_perro

urlpatterns = [
    path('', home, name="home"),
    path('alimentos_secos_perro/', alimentos_secos_perro, name="alimentos_secos_perro"),
]