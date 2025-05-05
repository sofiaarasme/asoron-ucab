from django import forms
from core.inventario.models import *

class BotellaForm(forms.ModelForm):
    class Meta:
        model = Botella
        fields = ['botella_nombre','fk_ron', 'fk_tapa', 'fk_materia_prima', 'fk_proveedor', 'botella_precio', 'botella_capacidad', 'botella_ancho', 'botella_alto']

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['inventario_cantidad', 'fk_botella','fk_departamento', 'inventario_descripcion']