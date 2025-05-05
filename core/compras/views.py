from django.db import connection
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.http import HttpResponseNotFound
from datetime import date
from django.http import JsonResponse
from .models import Proveedor
import traceback

class ListaComprasViewS(generic.ListView):
    template_name = "compras/index.html"
    context_object_name = "lista_compras"

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM compra")
            rows = cursor.fetchall()

        return rows

class ListaComprasView(generic.ListView):
    template_name = "compras/index.html"
    context_object_name = "lista_compras"

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM compra")
            rows = cursor.fetchall()

        return rows

    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT fk_botella FROM inventario WHERE inventario_cantidad < 100")
            botellas_bajas = cursor.fetchall()

            if botellas_bajas:
                fk_botella = botellas_bajas[0][0]  # Ajusta el índice para obtener el fk_botella
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT b.botella_id, b.botella_nombre, b.fk_proveedor
                        FROM botella b
                        WHERE b.botella_id = %s
                    """, [fk_botella])
                    botella_info = cursor.fetchone()
                    proveedor_id = botella_info[2] if botella_info else None
                    botella_id = botella_info[0] if botella_info else None
                    botella_nombre = botella_info[1] if botella_info else None

                fecha_emision = date.today().strftime("%Y-%m-%d")
                descripcion = "Orden de reposicion por cantidad menor a 100 unidades."
                context = {
                    'proveedor': proveedor_id,
                    'botella_id': botella_id,
                    'botella_nombre': botella_nombre,
                    'fecha_emision': fecha_emision,
                    'descripcion': descripcion,
                }
                

                return render(self.request, 'compras/orden_reposicion.html', context)
            else:
                # Renderizar la vista 'index.html' si no hay botellas bajas
                return super().get(request, *args, **kwargs)
            
    def post(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT fk_botella FROM inventario WHERE inventario_cantidad < 100")
            botellas_bajas = cursor.fetchall()

            if botellas_bajas:
                fk_botella = botellas_bajas[0][0]  # Ajusta el índice para obtener el fk_botella
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT b.botella_id, o.orden_reposicion_id, b.fk_proveedor
                        FROM botella b, orden_reposicion o
                        WHERE b.botella_id = %s and o.fk_proveedor = b.fk_proveedor
                    """, [fk_botella])
                    botella_info = cursor.fetchone()
                    proveedor_id = botella_info[2] if botella_info else None
                    botella_id = botella_info[0] if botella_info else None
                    orden_reposicion_id = botella_info[1] if botella_info else None
                    print(proveedor_id, botella_id, orden_reposicion_id)

                    cursor.execute("call confirmar_orden_reposicion(%s, %s, %s)", [proveedor_id, botella_id,orden_reposicion_id])
        # Redirige a la misma vista después de procesar el formulario
        return self.get(request, *args, **kwargs)
            
  


    
def consultar_compra(request, compra_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM compra WHERE compra_num = %s", [compra_id])
        compra = cursor.fetchone()
        
        cursor.execute("SELECT * FROM detalle_compra WHERE FK_Compra = %s", [compra_id])
        detalles_compra = cursor.fetchall()

    if not compra:
        return HttpResponseNotFound("La compra no existe")

    context = {'compra': compra, 'detalles_compra': detalles_compra}
    return render(request, 'compras/consultar_compra.html', context)

def obtener_numero_compra():
    with connection.cursor() as cursor:
        cursor.execute("SELECT compra_num FROM compra ORDER BY compra_num DESC LIMIT 1")
        numero_compra = cursor.fetchone()

    if numero_compra is None:
        return 1
    else:
        return numero_compra[0] + 1

def obtener_botellas_de_proveedor(proveedor_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT B.botella_id, B.botella_nombre, B.botella_precio, B.botella_capacidad
            FROM Botella B
            WHERE B.fk_proveedor = %s
        """, [proveedor_id])
        botellas_del_proveedor = cursor.fetchall()
    
    return botellas_del_proveedor

def crear_orden(request):
    numero_compra = obtener_numero_compra()
    fecha_actual = date.today().strftime("%Y-%m-%d")
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM proveedor")
        proveedores = cursor.fetchall()

    context = {
        'numero_compra': numero_compra,
        'proveedores': proveedores,
        'fecha_actual': fecha_actual
    }
    return render(request, 'compras/crear_orden.html', context)

def obtener_proveedor(request, proveedor_id):
    try:
        proveedor = Proveedor.objects.get(pk=proveedor_id)
        botellas_del_proveedor = obtener_botellas_de_proveedor(proveedor_id)
        
        data = {
            'proveedor': {
                'nombre': proveedor.proveedor_razon_social,
                'id': proveedor.proveedor_id,
            },
            'botellas_del_proveedor': botellas_del_proveedor
        }
        return JsonResponse(data)
    except Proveedor.DoesNotExist:
        return JsonResponse({'error': 'Proveedor no encontrado'}, status=404)
    except Exception as e:
        print(traceback.format_exc())
        return JsonResponse({'error': 'Hubo un error en el servidor'}, status=500)


def registrar_compra(request):
    primera_vez = True
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor_id')
        fecha = request.POST.get('fecha')
        total = request.POST.get('total')
        tabla_productos = request.POST.getlist('tabla_productos[]')
        
        print(request.POST)
        
        with connection.cursor() as cursor:
            try:
                for producto in tabla_productos:
                    botella_id, precio, cantidad  = producto.split(',')
                    if primera_vez:                        
                        cursor.execute("CALL registrar_compra(%s, %s, %s, %s)", [proveedor_id, fecha, total, 0])
                        row = cursor.fetchone()
                        compra_num = row[0] if row else None
                        primera_vez = False
                    cantidad, precio, botella_id = producto.split(',')
                    cursor.execute("CALL registrar_detalle_compra(%s, %s, %s, %s)", [compra_num, precio, botella_id, cantidad])
                return render(request, 'compras/orden_exitosa.html')
            except Exception as e: 
                return render(request, 'compras/orden_exitosa.html')
            
    return render(request, 'compras/orden_exitosa.html')