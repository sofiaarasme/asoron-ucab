from django import forms
from core.facturacion.models import Tarjeta


class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['tarjeta_numero', 'tarjeta_cvv', 'tarjeta_fecha_vencimiento','tarjeta_banco']