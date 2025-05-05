from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'clientes'

urlpatterns = [
    path("", RedirectView.as_view(url='natural/', permanent=False)),
    path("natural/", views.IndexView.as_view(), name="index"),
    path("natural/registrar_cliente_natural/", views.ClienteNaturalCreateView.as_view(), name = "registrar_cliente_natural"),
    path("natural/<int:pk>/", views.ClienteNaturalConsultarView.as_view(), name="consultar_cliente_natural"),
    path("natural/<int:cliente_n_rif_anterior>/modificar", views.natural_modificar, name= "modificar_cliente_natural"),
    path("natural/<int:cliente_n_rif>/eliminar/", views.eliminar_natural_view, name= "eliminar_cliente_natural"),
    # path('natural/<int:pk>/eliminar/', views.ClienteNaturalDeleteView.as_view(), name= "eliminar_cliente_natural"),
    path('natural/<int:pk>/agregar_telefono', views.TelefonoCreateView.as_view(), name = "agregar_telefono"),
    path('natural/<int:pk>/agregar_correo', views.CorreoCreateView.as_view(), name = "agregar_correo"),
    path('juridico/', views.IndexJuridicoView.as_view(), name='index_juridico'),
    path('juridico/registrar_juridico/', views.ClienteJuridicoCreateView.as_view(), name='registrar_juridico'),
    path('juridico/<int:pk>/', views.ClienteJuridicoConsultarView.as_view(), name='consultar_juridico'),
    path('juridico/<int:cliente_j_rif_anterior>/modificar', views.juridico_modificar, name='modificar_juridico'),
    path('juridico/<int:cliente_j_rif>/eliminar/', views.eliminar_juridico_view, name='eliminar_juridico'),
    # path('juridico/<int:pk>/eliminar/', views.ClienteJuridicoDeleteView.as_view(), name='eliminar_juridico'),
    path('juridico/<int:pk>/agregar_telefono', views.TelefonoJuridicoCreateView.as_view(), name='agregar_telefono_juridico'),
    path('juridico/<int:pk>/agregar_correo', views.CorreoJuridicoCreateView.as_view(), name='agregar_correo_juridico'),
    path('juridico/<int:pk>/agregar_contacto', views.PersonaContactoCreateView.as_view(), name='agregar_contacto'),
    path('juridico/<int:pk>/<int:pk_contacto>', views.TelefonoContactoCreateView.as_view(), name='telefono_contacto'),
]