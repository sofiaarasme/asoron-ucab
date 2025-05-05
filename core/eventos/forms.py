from django import forms
from .models import Evento, Entrada

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['evento_nombre', 'evento_fecha_inicio', 'evento_fecha_fin', 'evento_ubicacion', 'fk_lugar']

class EntradaForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, label='Cantidad de Entradas')
    precio = forms.DecimalField(min_value=0, label='Precio por Entrada')