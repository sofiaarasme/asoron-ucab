from django.http import HttpResponse, JsonResponse
from core.nomina.models import *
from core.contactos.models import *
from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db import connection
from .forms import EmpleadoForm, TelefonoForm, HorarioEmpleadoForm, BeneficioEmpleadoForm

from django.views.generic.edit import *
from django.contrib import messages

class IndexView(generic.ListView):
    template_name = "nomina/index.html"
    context_object_name = "lista_empleados"

    def get_queryset(self):
        """Return the last five published questions."""
        # queryset = Empleado.objects.prefetch_related('telefonos').all()
        queryset = Empleado.objects.all()
        return queryset



# class EmpleadoCreateView(generic.CreateView):
#     model = Empleado
#     form_class = EmpleadoForm
#     template_name = 'nomina/registrar_empleado.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context['formset'] = EmpleadoTelefonoFormset(self.request.POST, instance=self.object)
#         else:
#             initial_data = [{'numero': ''} for _ in range(2)]
#             context['formset'] = EmpleadoTelefonoFormset(instance=self.object)
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         formset = context['formset']
#         if formset.is_valid():
#             self.object = form.save()
#             formset.instance = self.object
#             formset.save()
#             return super().form_valid(form)
#         else:
#             return self.render_to_response(self.get_context_data(form=form))

#     def get_success_url(self):
#         return reverse('nomina:index')

class EmpleadoCreateView(generic.CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'nomina/registrar_empleado.html'
    
    def get_success_url(self):
        return reverse('nomina:index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Puedes agregar acciones adicionales si es necesario
        return response
    
class EmpleadoConsultarView(generic.DetailView):
    model = Empleado
    template_name = "nomina/consultar_empleado.html"
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        # Obtener el contexto base de la vista
        context = super().get_context_data(**kwargs)

        # Obtener el objeto Empleado actual
        empleado = context['empleado']

        with connection.cursor() as cursor1:
                cursor1.execute( """
                                select he.fk_horario
                                from horario_empleado he
                                where he.fk_empleado = %s""", [empleado.empleado_id])
                                
                rows = cursor1.fetchall()
    
                 # Obtener todos los fk_horario en una lista
                fk_horarios = [row[0] for row in rows] if rows else []

        print(empleado.empleado_id)
        print()
        horarios = Horario.objects.filter(horario_id__in=fk_horarios)

        # Agregar la lista de horarios_empleado al contexto
        context['horarios_empleado'] = horarios
        
        with connection.cursor() as cursor:
            cursor.execute("""
                                select be.fk_beneficio
                                from beneficio_empleado be
                                where be.fk_empleado = %s""", [empleado.empleado_id])

            rows_beneficios = cursor.fetchall()

            # Obtener todos los fk_beneficio en una lista
            fk_beneficios = [row[0] for row in rows_beneficios] if rows_beneficios else []

        # Agregar la lista de fk_beneficios al contexto
        context['beneficios_empleado'] = Beneficio.objects.filter(beneficio_id__in=fk_beneficios)

        return context

class EmpleadoModificarView(UpdateView):
    model = Empleado
    template_name = 'nomina/modificar_empleado.html'
    fields = ['empleado_ci', 'empleado_primer_nombre', 'empleado_segundo_nombre', 'empleado_primer_apellido', 'empleado_segundo_apellido', 'empleado_sueldo', 'empleado_cargo', 'fk_departamento', 'fk_tienda']
    success_url = reverse_lazy('nomina:index')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'nomina/eliminar_empleado.html'
    success_url = reverse_lazy('nomina:index')

class TelefonoCreateView(generic.CreateView):
    model = Telefono
    form_class = TelefonoForm
    template_name = 'nomina/agregar_telefono.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('nomina:index')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        empleado = get_object_or_404(Empleado, pk=self.kwargs['pk'])
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_empleado = empleado
        self.object.save()

        return super().form_valid(form)
        
def agregar_horario_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, empleado_id=empleado_id)
    if request.method == 'POST':
        form = HorarioEmpleadoForm(request.POST)
        if form.is_valid():
            horario = form.cleaned_data['fk_horario']
            fk_horario = horario.horario_id
            fk_empleado = empleado_id

            with connection.cursor() as cursor:
                cursor.execute("insert into horario_empleado (fk_horario, fk_empleado) values (%s,%s)", [fk_horario, fk_empleado])
            return redirect('nomina:consultar_empleado', empleado_id)
    else:
        form = HorarioEmpleadoForm()
    return render(request, 'nomina/agregar_horario.html', {'form': form})

def agregar_beneficio_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, empleado_id=empleado_id)
    if request.method == 'POST':
        form = BeneficioEmpleadoForm(request.POST)
        if form.is_valid():
            beneficio = form.cleaned_data['fk_beneficio']
            fk_beneficio = beneficio.beneficio_id
            fk_empleado = empleado_id

            with connection.cursor() as cursor:
                cursor.execute("insert into beneficio_empleado (fk_beneficio, fk_empleado) values (%s,%s)", [fk_beneficio, fk_empleado])
            return redirect('nomina:consultar_empleado', empleado_id)
    else:
        form = BeneficioEmpleadoForm()
    return render(request, 'nomina/agregar_beneficio.html', {'form': form})
    