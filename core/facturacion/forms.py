from django import forms
from .models import Punto, Conversion_divisa

class PuntoForm(forms.ModelForm):
    class Meta:
        model = Punto
        fields = ['punto_valor', 'punto_fecha_inicio', 'punto_fecha_fin']

class ConversionDivisaForm(forms.ModelForm):
    class Meta:
        model = Conversion_divisa
        fields = ['cd_valor', 'cd_fecha_inicio', 'cd_fecha_fin']