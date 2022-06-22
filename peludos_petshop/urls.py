from django.urls import path
from .views import home, alimentos_secos_perro, alimentos_humedos_perro, snack_perro, juguete_perro, alimentos_secos_gato, alimentos_humedos_gato, arena_sanitaria_gato, \
    snack_gato, juguete_gato, alimentos_conejo, accesorios_conejo, alimentos_erizo, accesorios_erizo, alimentos_hamster, accesorios_hamster, alimentos_hurron, accesorios_hurron, \
    detalle_producto, home_admin, agregar_productos, eliminar_producto, modificar_productos, registro_usuario,  registrar_contacto, lista_contactos, eliminar_contacto, \
    listar_productos, carrito_de_compras

urlpatterns = [
    path('', home, name="home"),
    path('home_admin/', home_admin, name="home_admin"),
    path('alimentos_secos_perro/', alimentos_secos_perro, name="alimentos_secos_perro"),
    path('alimentos_humedos_perro/', alimentos_humedos_perro, name="alimentos_humedos_perro"),
    path('snack_perro/', snack_perro, name="snack_perro"),
    path('juguete_perro/', juguete_perro, name="juguete_perro"),
    path('alimentos_secos_gato/', alimentos_secos_gato, name="alimentos_secos_gato"),
    path('alimentos_humedos_gato/', alimentos_humedos_gato, name="alimentos_humedos_gato"),
    path('arena_sanitaria_gato/', arena_sanitaria_gato, name="arena_sanitaria_gato"),
    path('snack_gato/', snack_gato, name="snack_gato"),
    path('juguete_gato/', juguete_gato, name="juguete_gato"),
    path('alimentos_conejo/', alimentos_conejo, name="alimentos_conejo"),
    path('accesorios_conejo/', accesorios_conejo, name="accesorios_conejo"),
    path('alimentos_erizo/', alimentos_erizo, name="alimentos_erizo"),
    path('accesorios_erizo/', accesorios_erizo, name="accesorios_erizo"),
    path('alimentos_hamster/', alimentos_hamster, name="alimentos_hamster"),
    path('accesorios_hamster/', accesorios_hamster, name="accesorios_hamster"),
    path('alimentos_hurron/', alimentos_hurron, name="alimentos_hurron"),
    path('accesorios_hurron/', accesorios_hurron, name="accesorios_hurron"),
    path('detalle_producto/<str:id>', detalle_producto, name="detalle_producto"),
    path('agregar_productos/', agregar_productos, name="agregar_productos"),
    path('eliminar/<int:id>',eliminar_producto, name="eliminar_producto"),
    path('modificar_productos/<id>/', modificar_productos, name="modificar_productos"),
    path('registro_usuario', registro_usuario, name="registro_usuario"),
    path('registro_contacto', registrar_contacto, name="registro_contacto"),
    path('Listado_contactos', lista_contactos, name="lista_contactos"),
    path('eliminar_contacto/<int:id_contacto>',eliminar_contacto, name="eliminar_contacto"),
    path('listado_productos/', listar_productos, name="listar_productos"),
    path('carrito_de_compras/', carrito_de_compras, name="carrito_de_compras"),
]