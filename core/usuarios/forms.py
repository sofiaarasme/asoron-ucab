from django import forms
from .models import Usuario
from .models import Rol
from .models import Permiso

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario_nombre', 'usuario_contrasena','fk_empleado']

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['rol_nombre', 'rol_descripcion', 'permisos']

    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'permisos-select'})
    )

class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ['permiso_nombre', 'permiso_tipo']