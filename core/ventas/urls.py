from django.urls import path

from . import views

app_name = 'ventas'

urlpatterns = [
    path("", views.ListaVentasView.as_view(), name="index"),
    path("<int:venta_id>/", views.consultar_venta, name="consultar_venta"),
    path("categoria/", views.ListaCategoriaView.as_view(), name="lista_por_categoria"),
    path("puntos/", views.lista_ventas_con_puntos, name="lista_por_puntos"),
]