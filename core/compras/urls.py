from django.urls import path

from . import views

app_name = 'compras'

urlpatterns = [
    path("", views.ListaComprasView.as_view(), name="index"),
    path("scompras/", views.ListaComprasViewS.as_view(), name="index_sin_orden"),
    path("<int:compra_id>/", views.consultar_compra, name="consultar_compra"),
    path("crear_orden/", views.crear_orden, name="crear_orden"),
    path("obtener_proveedor/<int:proveedor_id>/", views.obtener_proveedor, name="obtener_proveedor"),
    path("registrar_compra/", views.registrar_compra, name='registrar_compra'),
    
]