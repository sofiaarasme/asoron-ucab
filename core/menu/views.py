from django.shortcuts import render, redirect
from core.usuarios.models import Usuario, UsuarioRol

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Usuario.objects.filter(usuario_nombre=username, usuario_contrasena=password).first()

        if user is not None:

            user_rol = UsuarioRol.objects.filter(fk_usuario=user).first()

            if user_rol:
                if user_rol.fk_rol.rol_id == 1:
                    return redirect('http://127.0.0.1:8000/menu/admin_menu')
                elif user_rol.fk_rol.rol_id == 2:
                    return redirect('http://127.0.0.1:8000/menu/ventas_menu')
                elif user_rol.fk_rol.rol_id == 3:
                    return redirect('http://127.0.0.1:8000/menu/compras_menu')
                elif user_rol.fk_rol.rol_id == 4:
                    return redirect('http://127.0.0.1:8000/menu/promociones_menu')
                elif user_rol.fk_rol.rol_id == 5:
                    return redirect('http://127.0.0.1:8000/sitioweb')

    return render(request, 'login.html')


def admin_menu(request):
    return render(request, 'header.html', {'current_view': 'admin_menu'})

def ventas_menu(request):
    return render(request, 'header.html', {'current_view': 'ventas_menu'})

def compras_menu(request):
    return render(request, 'header.html', {'current_view': 'compras_menu'})

def promociones_menu(request):
    return render(request, 'header.html', {'current_view': 'promociones_menu'})

def cliente_view(request):
    return render(request, 'cliente_view.html')



def admin_menu(request):
    return render(request, 'menu.html')

def register_view(request):
    return render(request, 'register.html')

def ventas_menu(request):
    return render(request, 'ventas_menu.html')

def promociones_menu(request):
    return render(request, 'promociones_menu.html')

def compras_menu(request):
    return render(request, 'compras_menu.html')

def cliente_view(request):
    return render(request, 'cliente_view.html')