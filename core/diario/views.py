from django.shortcuts import render
from django.db import connection


def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT *, (botella_precio::numeric - valor_oferta::numeric) AS precio_resta FROM ofertas_view")
        productos = cursor.fetchall()
    return render(request, 'diario/index.html', {'productos': productos})



