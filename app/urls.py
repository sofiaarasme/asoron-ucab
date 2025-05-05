from core.nomina import views
from django.views.generic import RedirectView
"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.menu.views import login_view

urlpatterns = [
    # Redirección de la URL raíz a '/menu/admin_menu'
    path('', RedirectView.as_view(url='/menu/login/', permanent=True)),
    
    path('admin/', admin.site.urls),
    path('menu/', include("core.menu.urls")),
    path('nomina/', include("core.nomina.urls")),
    path('eventos/', include("core.eventos.urls")),
    path('clientes/', include("core.clientes.urls")),
    path('diario/', include("core.diario.urls")),
    path('dashboard/', include("core.dashboard.urls")),
    path('usuarios/', include("core.usuarios.urls")),
    path('inventario/', include("core.inventario.urls")),
    path('facturacion/', include("core.facturacion.urls")),
    path('sitioweb/', include("core.sitioweb.urls")),
    path('compras/', include("core.compras.urls")),
    path('ventas/', include("core.ventas.urls")),
]
