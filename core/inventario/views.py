from django.shortcuts import render
from core.inventario.models import *
from django.http import HttpResponse, JsonResponse
from core.nomina.models import *
from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import *
from django.db import connection, IntegrityError
from django.contrib import messages

class IndexView(generic.ListView):
    template_name = "inventario/index.html"
    context_object_name = "lista_inventario"

    def get_queryset(self):
        """Return the last five published questions."""
        # queryset = Empleado.objects.prefetch_related('telefonos').all()
        queryset = Inventario.objects.all()
        return queryset
    
class IndexProductoView(generic.ListView):
    template_name = "inventario/index_producto.html"
    context_object_name = "lista_botellas"

    def get_queryset(self):
        """Return the last five published questions."""
        # queryset = Empleado.objects.prefetch_related('telefonos').all()
        queryset = Botella.objects.all()
        return queryset
    
class IndexOfertasView(generic.ListView):
    template_name = "inventario/index_ofertas.html"
    context_object_name = "lista_ofertas"
    
    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ofertas_view")
            rows = cursor.fetchall()

        return rows
    
class BotellaCreateView(generic.CreateView):
    model = Botella
    form_class = BotellaForm
    template_name = 'inventario/registrar_producto.html'
    
    def get_success_url(self):
        return reverse('inventario:index_producto')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Puedes agregar acciones adicionales si es necesario
        return response
    
class BotellaConsultarView(generic.DetailView):
    model = Botella
    template_name = "inventario/consultar_producto.html"
    context_object_name = 'botella'

def eliminar_producto_sql(self, botella_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM botella WHERE botella_id = %s", [botella_id])

def eliminar_producto_view(request, botella_id):
    eliminar_producto_sql(request, botella_id)
    return redirect('inventario:index_producto')

def modificar_producto(request, botella_id):
    botella = get_object_or_404(Botella, botella_id=botella_id)

    if request.method == 'POST':
        formulario = BotellaForm(request.POST, instance=botella)
        if formulario.is_valid():
            formulario.save()
        return redirect('inventario:index_producto')
    else:
        formulario = BotellaForm(initial={ 'botella_nombre': botella.botella_nombre, 'fk_ron': botella.fk_ron, 'fk_tapa': botella.fk_tapa, 'fk_materia_prima': botella.fk_materia_prima, 'fk_proveedor': botella.fk_proveedor, 'botella_precio': botella.botella_precio, 'botella_capacidad': botella.botella_capacidad, 'botella_ancho': botella.botella_ancho, 'botella_alto': botella.botella_alto })

    return render(request, 'inventario/modificar_producto.html', {'formulario': formulario})

def registrar_inventario (request):
    if request.method == 'POST':
        formulario = InventarioForm(request.POST)
        if formulario.is_valid():
            inventario_cantidad = formulario.cleaned_data['inventario_cantidad']
            botella = formulario.cleaned_data['fk_botella']
            fk_botella = botella.botella_id
            departamento = formulario.cleaned_data['fk_departamento']
            fk_departamento = departamento.departamento_id
            inventario_descripcion = formulario.cleaned_data['inventario_descripcion']
            print(inventario_cantidad, fk_botella, fk_departamento, inventario_descripcion)

            with connection.cursor() as cursor:
                try:
                    cursor.execute("CALL registrar_inventario(%s, %s, %s, %s)", [inventario_cantidad, fk_botella, fk_departamento, inventario_descripcion])
                    messages.success(request, 'Inventario registrado')
                    return redirect('inventario:index')
                except IntegrityError as e:
                    print(f"Error al registrar el inventario en la base de datos: {e}")
                    messages.error(request, 'Error al registrar el inventario')
                    return JsonResponse({'error': 'Error al registrar el inventario'})
                
    else:
        # Si la solicitud no es un POST, crea un formulario vacío
        formulario = InventarioForm()

    return render(request, 'inventario/registrar_inventario.html', {'formulario': formulario})

class InventarioConsultarView(generic.DetailView):
    model = Inventario
    template_name = "inventario/consultar_inventario.html"
    context_object_name = 'inventario'

def ficha_producto(request, botella_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ficha_producto WHERE botella_id = %s", [botella_id])
        ficha = cursor.fetchone()
        print(ficha)
    return render(request, 'inventario/ficha_producto.html', {'ficha': ficha})