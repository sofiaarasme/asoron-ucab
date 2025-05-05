from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from core.clientes.models import *
from .forms import *
from core.contactos.models import Telefono, Correo, PersonaContacto 
from django.views.generic.edit import *
from django.contrib import messages
from django.db import connection

class IndexView(generic.ListView):
    template_name = "clientes/index.html"
    context_object_name = "lista_clientes_naturales"

    def get_queryset(self):
        """Return the last five published questions."""
        return Cliente_natural.objects.all

class ClienteNaturalCreateView(generic.CreateView):
    model = Cliente_natural
    form_class = ClienteNaturalForm
    template_name = 'clientes/registrar_cliente_natural.html'
    
    def get_success_url(self):
        return reverse('clientes:index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Puedes agregar acciones adicionales si es necesario
        return response
    
class ClienteNaturalConsultarView(generic.DetailView):
    model = Cliente_natural
    template_name = "clientes/consultar_cliente_natural.html"
    context_object_name = 'cliente'

# class ClienteNaturalModificarView(UpdateView):
#     model = Cliente_natural
#     template_name = 'clientes/modificar_cliente_natural.html'
#     fields = ['cliente_n_rif', 'cliente_cedula', 'cliente_p_nombre', 'cliente_s_nombre', 'cliente_p_apellido', 'cliente_s_apellido', 'cliente_direccion', 'fk_lugar']
#     success_url = reverse_lazy('clientes:index')

#####################################################################
# ROMEL ESTA FUE LA QUE TOQUÉ, NO TE MOLESTES TQMMM
def natural_modificar(request, cliente_n_rif_anterior):
    cliente = get_object_or_404(Cliente_natural, cliente_n_rif=cliente_n_rif_anterior)

    if request.method == 'POST':
        formulario = ClienteNaturalModificar(request.POST, instance=cliente)
        if formulario.is_valid():
            cliente.cliente_n_rif = formulario.cleaned_data['cliente_n_rif']
            cliente.cliente_cedula = formulario.cleaned_data['cliente_cedula']
            cliente.cliente_p_nombre = formulario.cleaned_data['cliente_p_nombre']
            cliente.cliente_s_nombre = formulario.cleaned_data['cliente_s_nombre']
            cliente.cliente_p_apellido = formulario.cleaned_data['cliente_p_apellido']
            cliente.cliente_s_apellido = formulario.cleaned_data['cliente_s_apellido']
            cliente.cliente_direccion = formulario.cleaned_data['cliente_direccion']
            Lugar = formulario.cleaned_data['fk_lugar']
            lugar_id = Lugar.lugar_id
            with connection.cursor() as cursor:
                cursor.execute("UPDATE cliente_natural SET cliente_n_rif = %s, cliente_cedula = %s, cliente_p_nombre = %s, cliente_s_nombre = %s, cliente_p_apellido = %s, cliente_s_apellido = %s, cliente_direccion = %s, fk_lugar = %s WHERE cliente_n_rif = %s", [cliente.cliente_n_rif, cliente.cliente_cedula, cliente.cliente_p_nombre, cliente.cliente_s_nombre, cliente.cliente_p_apellido, cliente.cliente_s_apellido, cliente.cliente_direccion, lugar_id, cliente_n_rif_anterior])
            return redirect('clientes:index')
    else:
        formulario = ClienteNaturalModificar(initial={ 'cliente_n_rif': cliente.cliente_n_rif, 'cliente_cedula': cliente.cliente_cedula, 'cliente_p_nombre': cliente.cliente_p_nombre, 'cliente_s_nombre': cliente.cliente_s_nombre, 'cliente_p_apellido': cliente.cliente_p_apellido, 'cliente_s_apellido': cliente.cliente_s_apellido, 'cliente_direccion': cliente.cliente_direccion, 'fk_lugar': cliente.fk_lugar })

    return render(request, 'clientes/modificar_cliente_natural.html', {'formulario': formulario})
#####################################################################

def eliminar_natural_sql(self, cliente_n_rif):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM cliente_natural WHERE cliente_n_rif = %s", [cliente_n_rif])

# class ClienteNaturalDeleteView(generic.DeleteView):
#     model = Cliente_natural
#     template_name = 'clientes/eliminar_cliente_natural.html'
#     success_url = reverse_lazy('clientes:index')

#     def get_object(self, queryset=None):
#         # Este método se utiliza para obtener el objeto a eliminar
#         obj = super().get_object(queryset=queryset)
#         print(f'RIF del cliente a eliminar: {obj.cliente_n_rif}')
#         eliminar_natural_sql(self, obj.cliente_n_rif)
#         return obj

def eliminar_natural_view(request, cliente_n_rif):
    eliminar_natural_sql(request, cliente_n_rif)
    return redirect('clientes:index')

class TelefonoCreateView(generic.CreateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = 'clientes/agregar_telefono_cliente_natural.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('clientes:index')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        empleado = get_object_or_404(Cliente_natural, pk=self.kwargs['pk'])
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_natural = empleado
        self.object.save()

        return super().form_valid(form)
    
class CorreoCreateView(generic.CreateView):
    model = Correo
    form_class = CorreoForm
    template_name = 'clientes/agregar_correo_natural.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('clientes:index')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        empleado = get_object_or_404(Cliente_natural, pk=self.kwargs['pk'])
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_natural = empleado
        self.object.save()

        return super().form_valid(form)

class IndexJuridicoView(generic.ListView):
    template_name = "clientes/index_juridico.html"
    context_object_name = "lista_clientes_juridicos"

    def get_queryset(self):
        """Return the last five published questions."""
        return Cliente_juridico.objects.all

class ClienteJuridicoCreateView(generic.CreateView):
    model = Cliente_juridico
    form_class = ClienteJuridicoForm
    template_name = 'clientes/registrar_juridico.html'
    
    def get_success_url(self):
        return reverse('clientes:index_juridico')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Puedes agregar acciones adicionales si es necesario
        return response
    
class ClienteJuridicoConsultarView(generic.DetailView):
    model = Cliente_juridico
    template_name = "clientes/consultar_juridico.html"
    context_object_name = 'cliente_j'

# class ClienteJuridicoModificarView(UpdateView):
#     model = Cliente_juridico
#     template_name = 'clientes/modificar_juridico.html'
#     fields = ['cliente_j_rif', 'cliente_denominacion_comercial', 'cliente_razon_social', 'cliente_pagina_web', 'cliente_capital_disponible', 'cliente_direccion_fiscal', 'cliente_direccion_fisica', 'fk_lugar']
#     success_url = reverse_lazy('clientes:index_juridico')

def juridico_modificar(request, cliente_j_rif_anterior):
    cliente = get_object_or_404(Cliente_juridico, cliente_j_rif=cliente_j_rif_anterior)

    if request.method == 'POST':
        formulario = ClienteJuridicoForm(request.POST, instance=cliente)
        if formulario.is_valid():
            cliente.cliente_j_rif = formulario.cleaned_data['cliente_j_rif']
            cliente.cliente_denominacion_comercial = formulario.cleaned_data['cliente_denominacion_comercial']
            cliente.cliente_razon_social = formulario.cleaned_data['cliente_razon_social']
            cliente.cliente_pagina_web = formulario.cleaned_data['cliente_pagina_web']
            cliente.cliente_capital_disponible = formulario.cleaned_data['cliente_capital_disponible']
            cliente.cliente_direccion_fiscal = formulario.cleaned_data['cliente_direccion_fiscal']
            cliente.cliente_direccion_fisica = formulario.cleaned_data['cliente_direccion_fisica']
            Lugar = formulario.cleaned_data['fk_lugar']
            lugar_id = Lugar.lugar_id

            with connection.cursor() as cursor:
                cursor.execute("UPDATE cliente_juridico SET cliente_j_rif = %s, cliente_denominacion_comercial = %s, cliente_razon_social = %s, cliente_pagina_web = %s, cliente_capital_disponible = %s, cliente_direccion_fiscal = %s, cliente_direccion_fisica = %s, fk_lugar = %s WHERE cliente_j_rif = %s", [cliente.cliente_j_rif, cliente.cliente_denominacion_comercial, cliente.cliente_razon_social, cliente.cliente_pagina_web, cliente.cliente_capital_disponible, cliente.cliente_direccion_fiscal, cliente.cliente_direccion_fisica, lugar_id, cliente_j_rif_anterior])
            return redirect('clientes:index_juridico')
    else:
        formulario = ClienteJuridicoForm(initial={ 'cliente_j_rif': cliente.cliente_j_rif, 'cliente_denominacion_comercial': cliente.cliente_denominacion_comercial, 'cliente_razon_social': cliente.cliente_razon_social, 'cliente_pagina_web': cliente.cliente_pagina_web, 'cliente_capital_disponible': cliente.cliente_capital_disponible, 'cliente_direccion_fiscal': cliente.cliente_direccion_fiscal, 'cliente_direccion_fisica': cliente.cliente_direccion_fisica, 'fk_lugar': cliente.fk_lugar })

    return render(request, 'clientes/modificar_juridico.html', {'formulario': formulario})

# class ClienteJuridicoDeleteView(generic.DeleteView):
#     model = Cliente_juridico
#     template_name = 'clientes/eliminar_juridico.html'
#     success_url = reverse_lazy('clientes:index_juridico')

def eliminar_juridico_sql(self, cliente_j_rif):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM cliente_juridico WHERE cliente_j_rif = %s", [cliente_j_rif])

def eliminar_juridico_view(request, cliente_j_rif):
    eliminar_juridico_sql(request, cliente_j_rif)
    return redirect('clientes:index_juridico')

class TelefonoJuridicoCreateView(generic.CreateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = 'clientes/agregar_telefono_juridico.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('clientes:index_juridico')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        empleado = get_object_or_404(Cliente_juridico, pk=self.kwargs['pk'])
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_juridico = empleado
        self.object.save()

        return super().form_valid(form)
    
class CorreoJuridicoCreateView(generic.CreateView):
    model = Correo
    form_class = CorreoForm
    template_name = 'clientes/agregar_correo_juridico.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('clientes:index_juridico')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        empleado = get_object_or_404(Cliente_juridico, pk=self.kwargs['pk'])
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_juridico = empleado
        self.object.save()

        return super().form_valid(form)
    
class PersonaContactoCreateView(generic.CreateView):
    model = PersonaContacto
    form_class = PersonaContactoForm
    template_name = 'clientes/agregar_persona_contacto.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('clientes:index_juridico')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        empleado = get_object_or_404(Cliente_juridico, pk=self.kwargs['pk'])
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_juridico = empleado
        self.object.save()

        return super().form_valid(form)
    
class TelefonoContactoCreateView(generic.CreateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = 'clientes/agregar_telefono_contacto.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('clientes:index_juridico')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        contacto = get_object_or_404(PersonaContacto, pk=self.kwargs['pk_contacto'])
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_persona_contacto = contacto
        self.object.save()

        return super().form_valid(form)
        
        