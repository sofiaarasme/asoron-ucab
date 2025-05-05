""" from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios' """

from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    name = 'core.usuarios'  # Asegúrate de que 'core.usuarios' sea la ruta correcta a tu aplicación 'usuarios'
    verbose_name = 'Usuarios'