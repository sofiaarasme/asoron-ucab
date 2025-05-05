from django.urls import path
from .views import *
from . import views

app_name = 'usuarios'

urlpatterns = [
    ###### URLS DE USUARIO ######
    path("", views.IndexView.as_view(), name="index"),
    path('usuarios/crear/', UserCreateView.as_view(), name='registrar_usuario'),
    path("<int:pk>/", views.UserReadView.as_view(), name="consultar_usuario"),
    ###### URLS DE ROL ######
    path("roles/", views.IndexRolView.as_view(), name="index_roles"),
    path('roles/crear/', RolCreateView.as_view(), name='registrar_rol'),
    path("roles/<int:pk>/", views.RolReadView.as_view(), name="consultar_rol"),
    path('roles/<int:pk>/editar/', RolUpdateView.as_view(), name='modificar_rol'),
    path('roles/<int:pk>/eliminar/', RolDeleteView.as_view(), name='eliminar_rol'),
    ###### URLS DE PERMISO ######
    path("permisos/", views.IndexPermisoView.as_view(), name="index_permisos"),
    path('permisos/crear/', PermisoCreateView.as_view(), name='registrar_permiso'),
    path("permisos/<int:pk>/", views.PermisoReadView.as_view(), name="consultar_permiso"),
    path('permisos/<int:pk>/editar/', PermisoUpdateView.as_view(), name='modificar_permiso'),
    path('permisos/<int:pk>/eliminar/', PermisoDeleteView.as_view(), name='eliminar_permiso'),
]
