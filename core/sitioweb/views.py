from django.shortcuts import render, redirect
from core.inventario.models import Botella
from core.eventos.models import Evento
from core.clientes.models import Cliente_juridico, Cliente_natural
from core.facturacion.models import Tarjeta
from core.facturacion.models import *
from .forms import *
from django.db import connection
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg


def index(request):
    return render(request, 'sitioweb/index.html')

def productos(request):
    productos = Botella.objects.all()
    return render(request, 'sitioweb/productos.html', {'productos': productos})

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'sitioweb/eventos.html', {'eventos': eventos})


def obtener_cantidad_entradas(evento_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL obtener_cantidad_entradas(%s, %s)", [evento_id, 0])
        row = cursor.fetchone()
        cantidad_entradas = row[0] if row else None
    return cantidad_entradas

def obtener_precio_entrada(evento_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL obtener_precio_entrada(%s, %s)", [evento_id, 0])
        row = cursor.fetchone()
        precio_entrada = row[0] if row else None
    return precio_entrada

def info_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    cantidad_entradas = obtener_cantidad_entradas(evento_id)
    precio_entrada = obtener_precio_entrada(evento_id)
    return render(request, 'sitioweb/info_evento.html', {'evento': evento, 'cantidad_entradas': cantidad_entradas, 'precio_entrada': precio_entrada})

def realizar_compra(request, evento_id):
    if request.method == 'POST':
        cantidad_entradas = int(request.POST.get('cantidad_comprar'))
        precio_unitario = obtener_precio_entrada(evento_id)
        cliente_rif = 1

        with connection.cursor() as cursor:
            cursor.execute("CALL crear_venta_entrada(%s, %s, %s, %s)", [cliente_rif, evento_id, cantidad_entradas, precio_unitario])
            
        return render(request, 'sitioweb/compra_exitosa.html')  # Renderiza el template del modal    
    
    eventos = Evento.objects.all()
    return render(request, 'sitioweb/eventos.html', {'eventos': eventos})

def obtener_precio_botella(evento_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL obtener_precio_entrada(%s, %s)", [evento_id, 0])
        row = cursor.fetchone()
        precio_entrada = row[0] if row else None
    return precio_entrada

def info_botella(request, botella_id):
    botella = Botella.objects.get(pk=botella_id)
    cantidad_botellas = obtener_cantidad_producto(botella_id)
    return render(request, 'sitioweb/info_producto.html', {'botella': botella, 'cantidad_botellas': cantidad_botellas})

def obtener_cantidad_producto(botella_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL obtener_cantidad_botellas(%s, %s)", [botella_id, 0])
        row = cursor.fetchone()
        cantidad_botellas = row[0] if row else None
        print (cantidad_botellas)
    return cantidad_botellas

def realizar_compra_botella(request, botella_id):
    if request.method == 'POST':
        cantidad_botellas = int(request.POST.get('cantidad_comprar'))
        botella = Botella.objects.get(pk=botella_id)
        precio_unitario = botella.botella_precio

        with connection.cursor() as cursor:
            cursor.execute("CALL agregar_producto_al_carrito(%s, %s, %s)", [1, botella_id, cantidad_botellas])
            
        return render(request, 'sitioweb/agregado_exitoso.html')  # Renderiza el template del modal    
    
    return render(request, 'sitioweb/productos.html', {'producto': botella})

def carrito(request):
    cliente_id = 1  # ID del cliente

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT d.pedido_cantidad, d.pedido_precio_unitario, b.botella_nombre, b.botella_id
            FROM detalle_pedido d
            INNER JOIN presupuesto p ON d.fk_presupuesto = p.presupuesto_num
            INNER JOIN botella b ON d.fk_botella = b.botella_id 
            WHERE p.fk_natural = %s and p.fk_venta is null
            """,
            [cliente_id]
        )
        productos_carrito = cursor.fetchall()
        
        total_carrito = sum(producto[0] * producto[1] for producto in productos_carrito)
        total_fila = [producto[0] * producto[1] for producto in productos_carrito]
        productos_con_total = zip(productos_carrito, total_fila)

    return render(request, 'sitioweb/carrito.html', {'productos_carrito': productos_carrito, 'total_carrito': total_carrito, 'total_fila': total_fila, 'productos_con_total': productos_con_total})


def eliminar_producto(request, producto_id):
    cliente_id = 1 

    with connection.cursor() as cursor:
        cursor.execute("CALL eliminar_producto_carrito(%s, %s)", [producto_id, cliente_id])

    return redirect('sitioweb:carrito')

def modificar_cantidad(request, producto_id):
    cliente_id = 1
    nueva_cantidad = request.POST.get('nueva_cantidad')

    with connection.cursor() as cursor:
        cursor.execute("CALL modificar_cantidad_carrito(%s, %s, %s)", [producto_id, cliente_id, nueva_cantidad])

    return redirect('sitioweb:carrito')

def seleccionar_tarjeta(request):
    rif_cliente = 1
    # lista_tarjetas = Tarjeta.objects.filter(fk_cliente=rif_cliente)
    cliente = Cliente_natural.objects.get(pk=rif_cliente)

    return render(request, 'sitioweb/seleccionar_tarjeta.html', {'cliente': cliente})

class TarjetaCreateView(generic.CreateView):
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'sitioweb/registrar_tarjeta.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('sitioweb:seleccionar_tarjeta')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        cliente = get_object_or_404(Cliente_natural, pk=1)
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_natural = cliente
        self.object.save()

        return super().form_valid(form)
    
def confirmar_pago(request, tarjeta_id):
    cliente = get_object_or_404(Cliente_natural, pk=1)  # Usando el id 1 como predeterminado
    tarjeta = get_object_or_404(Tarjeta, pk=tarjeta_id)
    with connection.cursor() as cursor:
        cursor.execute(
            """
            select presupuesto_monto_total
            from presupuesto
            where fk_natural = %s and fk_venta is null
            """,
            [cliente.cliente_n_rif]
        )
        row = cursor.fetchone()
        presupuesto_monto_total = row[0] if row else None

   
        cursor.execute(
        """
        select punto_valor
        from punto
        order by punto_id desc
        """,
        )
        row1 = cursor.fetchone()
        punto_valor = row1[0] if row else None

    return render(request, 'sitioweb/confirmar_pago_carrito.html', {'cliente': cliente, 'tarjeta': tarjeta, 'monto_total': presupuesto_monto_total, 'punto_valor': punto_valor})

def pagar_carrito(request, tarjeta_id):
    if request.method == 'POST':
        cantidad_puntos = int(request.POST.get('cantidad_comprar'))
        tarjeta = Tarjeta.objects.get(pk=tarjeta_id)
        cliente = Cliente_natural.objects.get(pk=1)
        print(tarjeta_id)
        print(cliente.cliente_n_rif)
        print(cantidad_puntos)

        with connection.cursor() as cursor:
            cursor.execute("CALL pagar_carrito(%s, %s, %s)", [tarjeta_id, cliente.cliente_n_rif, cantidad_puntos])
            print("hola")
            
        return render(request, 'sitioweb/pago_exitoso.html')  # Renderiza el template del modal    
    
    return render(request, 'sitioweb/productos.html', {'producto': 0})

def afiliacion(request):
    return render(request, 'sitioweb/afiliacion.html')

def seleccionar_tarjeta_afiliacion(request):
    rif_cliente = 1
    # lista_tarjetas = Tarjeta.objects.filter(fk_cliente=rif_cliente)
    cliente = Cliente_natural.objects.get(pk=rif_cliente)

    return render(request, 'sitioweb/seleccionar_tarjeta_afiliacion.html', {'cliente': cliente})

class TarjetaAfiliacionCreateView(generic.CreateView):
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'sitioweb/registrar_tarjeta_afiliacion.html'
    
    def get_success_url(self):
        # Cambia 'consulta_empleado' por 'consultar_empleado'
        return reverse('sitioweb:seleccionar_tarjeta_afiliacion')
    
    def form_valid(self, form):
        # Obtén el objeto Empleado al que deseas asociar el teléfono
        cliente = get_object_or_404(Cliente_natural, pk=1)
        
        # Guarda el teléfono y asócialo al empleado
        self.object = form.save(commit=False)
        self.object.fk_natural = cliente
        self.object.save()

        return super().form_valid(form)
    
def confirmar_pago(request, tarjeta_id):
    cliente = get_object_or_404(Cliente_natural, pk=1)  # Usando el id 1 como predeterminado
    tarjeta = get_object_or_404(Tarjeta, pk=tarjeta_id)
    with connection.cursor() as cursor:
        cursor.execute(
            """
            select presupuesto_monto_total
            from presupuesto
            where fk_natural = %s and fk_venta is null
            """,
            [cliente.cliente_n_rif]
        )
        row = cursor.fetchone()
        presupuesto_monto_total = row[0] if row else None

   
        cursor.execute(
        """
        select punto_valor
        from punto
        order by punto_id desc
        """,
        )
        row1 = cursor.fetchone()
        punto_valor = row1[0] if row else None

    return render(request, 'sitioweb/confirmar_pago_carrito.html', {'cliente': cliente, 'tarjeta': tarjeta, 'monto_total': presupuesto_monto_total, 'punto_valor': punto_valor})