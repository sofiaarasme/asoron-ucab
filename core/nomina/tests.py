from app.wsgi import *
from core.nomina.models import *

#Listar

# #Select * from Tabla
# query = Departamento.objects.all()
# print(query)

#Insercion en tabla
E = Empleado(empleado_id = 1,empleado_ci = '23908775', empleado_primer_nombre= 'Pedro', empleado_primer_apellido = 'Perez', FK_Departamento_id = '1').save()
E1 = Empleado(empleado_id = 2,empleado_ci = '12908770', empleado_primer_nombre= 'Maria', empleado_primer_apellido = 'Gonzalez', FK_Departamento_id = '2').save()
E2 = Empleado(empleado_id = 3,empleado_ci = '18908774', empleado_primer_nombre= 'Juan', empleado_primer_apellido = 'Ramirez', FK_Departamento_id = '3').save()


# #Edicion
# d = Departamento.objects.get(departamento_id=1)
# d.departamento_nombre='Ventas'
# d.save()

# #Eliminacion
# d = Departamento.objects.get(departamento_id=4)
# d.delete()

# obj = Departamento.objects.filter(departamento_nombre__contains = 'Pr')
# print(obj)

obj = Departamento.objects.filter(departamento_nombre__in=['Ventas', 'Compras']).count()
print(obj)