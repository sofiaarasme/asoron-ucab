from django import forms
from .models import Cliente_natural, Cliente_juridico
from core.nomina.models import Lugar
from core.contactos.models import Telefono, Correo, PersonaContacto

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['telefono_codigo', 'telefono_numero']

class ClienteNaturalForm(forms.ModelForm):
    class Meta:
        model = Cliente_natural
        fields = ['cliente_n_rif' ,'cliente_cedula','cliente_p_nombre', 'cliente_s_nombre', 'cliente_p_apellido', 'cliente_s_apellido', 'cliente_direccion', 'fk_lugar']

class ClienteJuridicoForm(forms.ModelForm):
    class Meta:
        model = Cliente_juridico
        fields = ['cliente_j_rif', 'cliente_denominacion_comercial', 'cliente_razon_social', 'cliente_pagina_web', 'cliente_capital_disponible', 'cliente_direccion_fiscal', 'cliente_direccion_fisica', 'fk_lugar']

class ClienteNaturalModificar(forms.ModelForm):
    class Meta:
        model = Cliente_natural
        fields = ['cliente_n_rif', 'cliente_cedula','cliente_p_nombre', 'cliente_s_nombre', 'cliente_p_apellido', 'cliente_s_apellido', 'cliente_direccion', 'fk_lugar']

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ['correo_direccion']

class PersonaContactoForm(forms.ModelForm):
    class Meta:
        model = PersonaContacto
        fields = ['contacto_nombre', 'contacto_apellido', 'contacto_cargo']