from django.urls import path

from . import views

app_name = 'nomina'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("registrar_empleado/", views.EmpleadoCreateView.as_view(), name = "registrar_empleado"),
    path("<int:pk>/", views.EmpleadoConsultarView.as_view(), name="consultar_empleado"),
    path("<int:pk>/modificar", views.EmpleadoModificarView.as_view(), name= "modificar_empleado"),
    path('<int:pk>/eliminar/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
    path('<int:pk>/agregar_telefono', views.TelefonoCreateView.as_view(), name = "agregar_telefono"),
    path('<int:empleado_id>/agregar_horario', views.agregar_horario_empleado, name = "agregar_horario"),
    path('<int:empleado_id>/agregar_beneficio', views.agregar_beneficio_empleado, name = "agregar_beneficio"),
    # #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]