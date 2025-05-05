from django.shortcuts import render
from django.db import connection
from datetime import datetime, timedelta

def index(request):
    try:
        if 'filter_button' in request.GET:
            fecha_desde = request.GET.get('fecha_desde')
            fecha_hasta = request.GET.get('fecha_hasta')
        else:
            fecha_hasta = datetime.now().strftime('%Y-%m-%d')
            fecha_desde = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        with connection.cursor() as cursor:
            cursor.execute("CALL botella_mas_vendida(%s,%s,%s)", [fecha_desde, fecha_hasta, '0'])
            result_botella_mas_vendida = cursor.fetchone()

            cursor.execute("CALL ventas_hasta_ahora(%s,%s,%s)", [fecha_desde, fecha_hasta, 0])
            result_numero_ventas = cursor.fetchone()

            cursor.execute('''
                            SELECT
                                botella.botella_nombre,
                                COUNT(*) AS repeticiones
                            FROM
                                detalle_venta
                            JOIN
                                botella ON detalle_venta.fk_botella = botella.botella_id
                            JOIN
                                venta ON detalle_venta.fk_venta = venta.venta_num
                            WHERE
                                detalle_venta.fk_tienda = 1
                                AND venta.venta_fecha BETWEEN %s AND %s
                            GROUP BY
                                botella.botella_nombre
                            ORDER BY
                                COUNT(*) DESC
                            LIMIT 10;
                        ''', [fecha_desde, fecha_hasta])
            result_top_botellas = cursor.fetchall()
            
            cursor.execute("CALL obtener_puntos_otorgados(%s,%s,%s)", [fecha_desde, fecha_hasta, 0])
            puntos_otorgados = cursor.fetchone()

            cursor.execute("CALL obtener_puntos_canjeados(%s,%s,%s)", [fecha_desde,fecha_hasta, 0])
            puntos_canjeados = cursor.fetchone()

        labels = [row[0] for row in result_top_botellas]
        data = [row[1] for row in result_top_botellas]

        return render(request, 'dashboard/index.html', {
            'botella_mas_vendida': result_botella_mas_vendida,
            'numero_ventas': result_numero_ventas,
            'labels': labels,
            'data': data,
            'fecha_desde': fecha_desde,
            'fecha_hasta': fecha_hasta,
            'puntos_otorgados': puntos_otorgados,
            'puntos_canjeados': puntos_canjeados
        })
    except Exception as e:
        print(f"Error en la vista: {e}")
        raise


