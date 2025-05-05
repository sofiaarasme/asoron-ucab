from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db import connection
from django.views import generic
from django.http import HttpResponseNotFound
from datetime import date
from django.http import JsonResponse
from django.db import IntegrityError
from .models import *
from .forms import *
from django.contrib import messages

class ListaFacturasView(generic.ListView):
    template_name = "facturacion/index.html"
    context_object_name = "lista_facturas"

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vista_venta WHERE fk_evento = 0 OR fk_evento IS NULL")
            rows = cursor.fetchall()
        return rows
    
def consultar_factura(request, venta_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM vista_venta WHERE venta_num = %s AND (fk_evento = 0 OR fk_evento IS NULL)", [venta_id])
        factura = cursor.fetchone()
        
        cursor.execute("SELECT * FROM detalle_venta WHERE FK_Venta = %s", [venta_id])
        detalles_venta = cursor.fetchall()

    if not factura:
        return HttpResponseNotFound("La venta no existe")
    
    cliente_rif = factura[4] if factura[4] is not None else factura[5]
    
    print(cliente_rif)
    print(detalles_venta)

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM cliente_juridico WHERE cliente_j_rif = %s", [cliente_rif])
        cliente_juridico = cursor.fetchone()
        print("Cliente jurídico:", cliente_juridico)

        cursor.execute("SELECT * FROM cliente_natural WHERE cliente_n_rif = %s", [cliente_rif])
        cliente_natural = cursor.fetchone()
        print("Cliente natural:", cliente_natural)

    cliente_info = None

    if cliente_juridico:
        cliente_info = cliente_juridico
        cliente_info = ('Juridico',) + cliente_info[1:]
    elif cliente_natural:
        cliente_info = cliente_natural
        cliente_info = ('Natural',) + cliente_info[1:]

    print(factura)
    print(cliente_info)

    context = {'factura': factura, 'detalles_venta': detalles_venta, 'cliente_info': cliente_info}
    return render(request, 'facturacion/consultar_factura.html', context)



def obtener_numero_factura():
    with connection.cursor() as cursor:
        cursor.execute("SELECT venta_num FROM Venta ORDER BY venta_num DESC LIMIT 1")
        numero_factura = cursor.fetchone()[0]
    return numero_factura + 1

def obtener_inventario_con_precio():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT I.inventario_id, I.FK_Botella, I.inventario_cantidad, B.botella_precio
            FROM Inventario I
            INNER JOIN Botella B ON I.FK_Botella = B.botella_id
        """)
        inventario_con_precio = cursor.fetchall()
    
    return inventario_con_precio

def crear_factura(request):
    numero_factura = obtener_numero_factura()
    fecha_actual = date.today().strftime("%Y-%m-%d")
    inventario_con_precio = obtener_inventario_con_precio()
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM todos_clientes")
        clientes = cursor.fetchall()

    context = {
        'numero_factura': numero_factura,
        'clientes': clientes,
        'fecha_actual': fecha_actual,
        'inventario': inventario_con_precio
    }
    return render(request, 'facturacion/crear_factura.html', context)

def obtener_cantidad_producto(botella_id):
    with connection.cursor() as cursor:
        cursor.execute("CALL obtener_cantidad_botellas(%s, %s)", [botella_id, 0])
        row = cursor.fetchone()
        cantidad_botellas = row[0] if row else None
        print (cantidad_botellas)
    return cantidad_botellas

def registrar_venta(request):
    primera_vez = True
    if request.method == 'POST':
        rif_cliente = request.POST.get('rif')
        rif_cliente_int = int(rif_cliente) if rif_cliente else None
        fecha = request.POST.get('fecha')
        total = request.POST.get('total')
        tabla_productos = request.POST.getlist('tabla_productos[]')
        tabla_metodos = request.POST.getlist('tabla_metodos[]')
        
        with connection.cursor() as cursor:
            try:
                for producto in tabla_productos:
                    cantidad, precio, botella_id = producto.split(',')
                    if primera_vez:                        
                        cursor.execute("CALL registrar_venta(%s, %s, %s, %s)", [rif_cliente_int, fecha, total, 0])
                        row = cursor.fetchone()
                        venta_num = row[0] if row else None
                        primera_vez = False
                    cantidad, precio, botella_id = producto.split(',')
                    print('venta_num: ', venta_num)
                    cursor.execute("CALL registrar_detalle_venta(%s, %s, %s)", [venta_num, botella_id, cantidad])
                
                for metodo in tabla_metodos:
                        metodo_id, monto = metodo.split(',')
                        cursor.execute("CALL registrar_metodo_pago(%s, %s, %s)", [venta_num, metodo_id, monto])
                print("Ventas registradas exitosamente en la base de datos")
                messages.success(request, 'Factura creada')
                return render(request, 'facturacion/venta_exitosa.html')
            except Exception as e:
                print("Ventas registradas exitosamente en la base de datos")
                messages.success(request, 'Factura creada')
                return render(request, 'facturacion/venta_exitosa.html')
            
    return render(request, 'facturacion/venta_exitosa.html')


class PuntosIndexView(generic.ListView):
    template_name = "facturacion/index_puntos.html"
    context_object_name = "lista_puntos"

    def get_queryset(self):
        """Return the last five published questions."""
        return Punto.objects.all
    
def registrar_punto(request):
    if request.method == 'POST':
        # Si la solicitud es un POST, procesa los datos del formulario
        formulario = PuntoForm(request.POST)
        if formulario.is_valid():
            # Accede a los datos del formulario
            punto_valor = float(formulario.cleaned_data['punto_valor'])
            punto_fecha_inicio = formulario.cleaned_data['punto_fecha_inicio']
            punto_fecha_fin = formulario.cleaned_data['punto_fecha_fin']

            with connection.cursor() as cursor:
                try:
                    cursor.execute("CALL registrar_punto(%s, %s, %s)", [punto_valor, punto_fecha_inicio, punto_fecha_fin])
                    messages.success(request, 'Punto registrado')
                    return redirect('facturacion:index_puntos')
                except IntegrityError as e:
                    print(f"Error al registrar el punto en la base de datos: {e}")
                    messages.error(request, 'Error al registrar el punto')
                    return JsonResponse({'error': 'Error al registrar el punto'})
    else:
        # Si la solicitud no es un POST, crea un formulario vacío
        formulario = PuntoForm()

    return render(request, 'facturacion/registrar_punto.html', {'formulario': formulario})

class DivisasIndexView(generic.ListView):
    template_name = "facturacion/index_divisas.html"
    context_object_name = "lista_divisas"

    def get_queryset(self):
        """Return the last five published questions."""
        return Conversion_divisa.objects.all
    
def registrar_divisa(request):
    if request.method == 'POST':
        # Si la solicitud es un POST, procesa los datos del formulario
        formulario = ConversionDivisaForm(request.POST)
        if formulario.is_valid():
            # Accede a los datos del formulario
            cd_valor = float(formulario.cleaned_data['cd_valor'])
            cd_fecha_inicio = formulario.cleaned_data['cd_fecha_inicio']
            cd_fecha_fin = formulario.cleaned_data['cd_fecha_fin']

            with connection.cursor() as cursor:
                try:
                    cursor.execute("CALL registrar_divisa(%s, %s, %s)", [cd_valor, cd_fecha_inicio, cd_fecha_fin])
                    messages.success(request, 'Divisa registrado')
                    return redirect('facturacion:index_divisas')
                except IntegrityError as e:
                    print(f"Error al registrar el punto en la base de datos: {e}")
                    messages.error(request, 'Error al registrar el punto')
                    return JsonResponse({'error': 'Error al registrar el punto'})

    else:
        # Si la solicitud no es un POST, crea un formulario vacío
        formulario = ConversionDivisaForm()

    return render(request, 'facturacion/registrar_divisa.html', {'formulario': formulario})

def venta_exitosa(request):
    return render(request, 'facturacion/venta_exitosa.html')

