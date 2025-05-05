from django.urls import path

from . import views

app_name = 'diario'

urlpatterns = [
    path('', views.index, name='index'),
    
]