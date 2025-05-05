from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from core.eventos.models import *
from .forms import EventoForm, EntradaForm
from django.views.generic.edit import *
from django.contrib import messages
from django.db import connection

class IndexView(generic.ListView):
    template_name = "eventos/index.html"
    context_object_name = "lista_eventos"

    def get_queryset(self):
        """Return the last five published questions."""
        return Evento.objects.all
    
class ConsultarView(generic.DetailView):
    model = Evento
    template_name = "eventos/consultar.html"
    context_object_name = 'evento'

class ModificarEventoView(UpdateView):
    model = Evento
    template_name = 'eventos/modificar.html'
    fields = ['evento_nombre', 'evento_fecha_inicio', 'evento_fecha_fin', 'evento_ubicacion', 'fk_lugar']
    success_url = reverse_lazy('eventos:index')

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'eventos/eliminar.html'
    success_url = reverse_lazy('eventos:index')

def index(request):
    lista_eventos = Evento.objects.all
    template = loader.get_template("eventos/index.html")
    context = {
        "lista_eventos": lista_eventos,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    lista_eventos = Evento.objects.all
    context = {"lista_eventos": lista_eventos}
    return render(request, "eventos/index.html", context)


class EventoCreateView(generic.CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/registrar_evento.html'
    
    def get_success_url(self):
        return reverse('eventos:index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Puedes agregar acciones adicionales si es necesario
        return response
    
def generar_entradas(request, evento_id):

    evento = get_object_or_404(Evento, pk=evento_id)

    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            precio = form.cleaned_data['precio']

            with connection.cursor() as cursor:
                cursor.execute("CALL generar_entradas(%s, %s, %s)", [cantidad, precio, evento.evento_id])
            return redirect('eventos:index')
    else:
        form = EntradaForm()

    return render(request, 'eventos/entradas.html', {'form': form})