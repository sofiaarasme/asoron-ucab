from django.urls import path

from . import views

app_name = 'inventario'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.InventarioConsultarView.as_view(), name="consultar_inventario"),
    path("registrar/", views.registrar_inventario, name="registrar_inventario"),
    path("productos/", views.IndexProductoView.as_view(), name="index_producto"),
    path("ofertas/", views.IndexOfertasView.as_view(), name="index_ofertas"),
    path("productos/registrar/", views.BotellaCreateView.as_view(), name="registrar_producto"),
    path("productos/<int:pk>/", views.BotellaConsultarView.as_view(), name="consultar_producto"),
    path("productos/<int:botella_id>/eliminar/", views.eliminar_producto_view, name="eliminar_producto"),
    path("productos/<int:botella_id>/modificar/", views.modificar_producto, name="modificar_producto"),
    path("productos/<int:botella_id>/ficha/", views.ficha_producto, name="ficha_producto"),
    
]