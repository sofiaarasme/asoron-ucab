from django.urls import path

from . import views

app_name = 'facturacion'

urlpatterns = [
    path("", views.ListaFacturasView.as_view(), name="index"),
    path("<int:venta_id>/", views.consultar_factura, name="consultar_facturacion"),
    path("crear_factura/", views.crear_factura, name = "crear_factura"),
    path("registrar_venta/", views.registrar_venta, name='registrar_venta'),
    path("puntos/", views.PuntosIndexView.as_view(), name="index_puntos"),
    path("puntos/registrar/", views.registrar_punto, name="registrar_punto"),
    path("divisas/", views.DivisasIndexView.as_view(), name="index_divisas"),
    path("divisas/registrar/", views.registrar_divisa, name="registrar_divisa"),
    path("venta_exitosa/", views.venta_exitosa, name="venta_exitosa"),
]