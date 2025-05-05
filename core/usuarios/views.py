from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views import generic

###### MANEJO DE USUARIOS ######
class IndexView(generic.ListView):
    template_name = "usuarios/index.html"
    context_object_name = "lista_usuarios"

    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    
class UserCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:index')
    
    def get_template_names(self):
        return ['usuarios/registrar_usuario.html'] 
    
class UserReadView(generic.DetailView):
    model = Usuario
    template_name = "usuarios/consultar_usuario.html"
    context_object_name = 'usuario'
    
###### MANEJO DE ROLES ######

class IndexRolView(generic.ListView):
    template_name = "usuarios/index_roles.html"
    context_object_name = "roles_con_permisos"

    def get_queryset(self):
        roles = Rol.objects.all()
        roles_con_permisos = []

        for rol in roles:
            permisos = RolPermiso.objects.filter(fk_rol=rol)
            roles_con_permisos.append({'rol': rol, 'permisos': permisos})

        return roles_con_permisos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RolCreateView(CreateView):
    model = Rol
    form_class = RolForm
    success_url = reverse_lazy('usuarios:index_roles')

    def get_template_names(self):
        return ['usuarios/registrar_rol.html']
    
    def form_valid(self, form):
        rol = form.save(commit=False)
        rol.save()
        permisos_seleccionados = form.cleaned_data.get('permisos')
        for permiso in permisos_seleccionados:
            RolPermiso.objects.create(fk_rol=rol, fk_permiso=permiso)
        return super().form_valid(form)
    
class RolReadView(generic.DetailView):
    model = Rol
    template_name = "usuarios/consultar_rol.html"
    context_object_name = 'rol'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rol = self.get_object()
        rol_permisos = RolPermiso.objects.filter(fk_rol=rol)
        context['rol_permisos'] = rol_permisos
        return context

class RolUpdateView(UpdateView):
    model = Rol
    form_class = RolForm
    success_url = reverse_lazy('usuarios:index_roles')  
    
    def get_template_names(self):
        return ['usuarios/modificar_rol.html']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rol = self.get_object()  # Obtener el objeto Rol
        context['rol'] = rol  # Agregar el objeto Rol al contexto
        return context
    
    def form_valid(self, form):
        rol = form.save(commit=False)
        rol.save()
        permisos_seleccionados = form.cleaned_data.get('permisos')

        # Obtiene los permisos existentes asociados a este rol
        permisos_actuales = RolPermiso.objects.filter(fk_rol=rol)

        # Lista los ids de los permisos actuales
        permisos_actuales_ids = [permiso.fk_permiso.pk for permiso in permisos_actuales]

        # Lista los ids de los permisos seleccionados
        permisos_seleccionados_ids = [permiso.pk for permiso in permisos_seleccionados]

        # Elimina los permisos que están en la base de datos pero no están seleccionados
        for permiso_id in permisos_actuales_ids:
            if permiso_id not in permisos_seleccionados_ids:
                RolPermiso.objects.filter(fk_rol=rol, fk_permiso_id=permiso_id).delete()

        # Agrega los nuevos permisos seleccionados
        for permiso in permisos_seleccionados:
            if permiso.pk not in permisos_actuales_ids:
                RolPermiso.objects.create(fk_rol=rol, fk_permiso=permiso)

        return super().form_valid(form)


class RolDeleteView(DeleteView):
    model = Rol
    success_url = reverse_lazy('usuarios:index_roles')
    template_name = 'usuarios/eliminar_rol.html'  

###### MANEJO DE PERMISOS ######

class IndexPermisoView(generic.ListView):
    template_name = "usuarios/index_permisos.html"
    context_object_name = "lista_permisos"

    def get_queryset(self):
        queryset = Permiso.objects.all()
        return queryset

class PermisoCreateView(CreateView):
    model = Permiso
    form_class = PermisoForm
    success_url = reverse_lazy('usuarios:index_permisos')

    def get_template_names(self):
        return ['usuarios/registrar_permiso.html']
    
class PermisoReadView(generic.DetailView):
    model = Permiso
    template_name = "usuarios/consultar_permiso.html"
    context_object_name = 'permiso'

class PermisoUpdateView(UpdateView):
    model = Permiso
    form_class = PermisoForm
    template_name = 'usuarios/modificar_permiso.html'  
    success_url = reverse_lazy('usuarios:index_permisos')  

class PermisoDeleteView(DeleteView):
    model = Permiso
    success_url = reverse_lazy('usuarios:index_permisos')
    template_name = 'usuarios/eliminar_permiso.html'