from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.views import generic
from django.http import HttpResponseNotFound

class ListaVentasView(generic.ListView):
    template_name = "ventas/index.html"
    context_object_name = "lista_ventas"

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vista_venta")
            rows = cursor.fetchall()
        return rows

class ListaCategoriaView(generic.ListView):
    template_name = "ventas/lista_por_categoria.html"
    context_object_name = "lista_por_categoria"

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM productos_vendidos_por_categoria")
            rows = cursor.fetchall()
        return rows

    
def consultar_venta(request, venta_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM vista_venta WHERE venta_num = %s", [venta_id])
        venta = cursor.fetchone()
        
        cursor.execute("SELECT * FROM vista_detalle_venta WHERE FK_Venta = %s", [venta_id])
        detalles_venta = cursor.fetchall()

    if not venta:
        return HttpResponseNotFound("La venta no existe")

    context = {'venta': venta, 'detalles_venta': detalles_venta}
    return render(request, 'ventas/consultar_venta.html', context)

def lista_ventas_con_puntos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM vista_venta_con_puntos")
        rows = cursor.fetchall()
    context = {'lista_ventas_con_puntos': rows}
    return render(request, 'ventas/lista_por_puntos.html', context)
