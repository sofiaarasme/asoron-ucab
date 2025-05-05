from django import forms
from core.nomina.models import *
from core.contactos.models import Telefono
from django.forms import inlineformset_factory

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['telefono_codigo', 'telefono_numero']

# EmpleadoTelefonoFormset = inlineformset_factory(Empleado, Telefono, form=TelefonoForm, extra=1, can_delete=True)

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['empleado_ci', 'empleado_primer_nombre', 'empleado_segundo_nombre', 'empleado_primer_apellido', 'empleado_segundo_apellido', 'empleado_sueldo', 'empleado_cargo', 'fk_departamento', 'fk_tienda']

class HorarioEmpleadoForm(forms.ModelForm):
    class Meta:
        model = HorarioEmpleado
        fields = ['fk_horario']

class BeneficioEmpleadoForm(forms.ModelForm):
    class Meta:
        model = BeneficioEmpleado
        fields = ['fk_beneficio']