from django.urls import path
from . import views

urlpatterns = [
    path('admin_menu/', views.admin_menu, name='admin_menu'),
    path('compras_menu/', views.compras_menu, name='compras_menu'),
    path('ventas_menu/', views.ventas_menu, name='ventas_menu'),
    path('promociones_menu/', views.promociones_menu, name='promociones_menu'),
    path('cliente_view/', views.cliente_view, name='cliente_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register'),
]