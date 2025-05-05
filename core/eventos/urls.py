from django.urls import path

from . import views

app_name = 'eventos'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("registrar_evento/", views.EventoCreateView.as_view(), name = "registrar_evento"),
    path("<int:pk>/", views.ConsultarView.as_view(), name="consultar"),
    path("<int:pk>/modificar", views.ModificarEventoView.as_view(), name= "modificar"),
    path('<int:pk>/eliminar/', views.EventoDeleteView.as_view(), name='eliminar'),
    path("<int:evento_id>/registrar_entrada/", views.generar_entradas, name = "registrar_entrada"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]