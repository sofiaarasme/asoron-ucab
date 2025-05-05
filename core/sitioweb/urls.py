from django.urls import path
from .views import *
from . import views

app_name = 'sitioweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('evento/<int:evento_id>/', views.info_evento, name='info_evento'),
    path('producto/<int:botella_id>/', views.info_botella, name='info_producto'),
    path('realizar_compra_botella/<int:botella_id>/', views.realizar_compra_botella, name='realizar_compra_botella'),
    path('realizar_compra/<int:evento_id>/', views.realizar_compra, name='realizar_compra'),
    path('eventos/', views.eventos, name='eventos'),
    path('carrito/', views.carrito, name='carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('carrito/modificar/<int:producto_id>/', views.modificar_cantidad, name='modificar_cantidad'),
    path('carrito/confirmar/', views.seleccionar_tarjeta, name='seleccionar_tarjeta'),
    path('carrito/confirmar/<int:tarjeta_id>/', views.confirmar_pago, name='confirmar_pago'),
    path('carrito/confirmar/<int:tarjeta_id>/pagar_carrito/', views.pagar_carrito, name='pagar_carrito'),
    path('carrito/registrar_tarjeta/', views.TarjetaCreateView.as_view(), name='registrar_tarjeta'),
    path('afiliacion/', views.afiliacion, name='afiliacion'),
    path('afiliacion/confirmar/', views.seleccionar_tarjeta_afiliacion, name='seleccionar_tarjeta_afiliacion'),
    path('afiliacion/registrar_tarjeta/', views.TarjetaAfiliacionCreateView.as_view(), name='registrar_tarjeta_afiliacion'),
]