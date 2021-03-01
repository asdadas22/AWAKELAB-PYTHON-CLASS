from django.shortcuts import render, redirect
from .forms import LoginForm
from .script import login
import Evaluacion_Medica as EM

# Create your views here.

def login_view(request):
    if request.method == "GET":
        login_form = LoginForm()
        context = {'login_form': login_form, 'Error': ''}
        return render(request, 'login.html', context)
    elif request.method == "POST":
        login_devuelto = LoginForm(request.POST)

        if login_devuelto.is_valid():
            datos_formulario_login = login_devuelto.cleaned_data
            usuario_devuelto = datos_formulario_login['usuario']
            pass_devuelto = datos_formulario_login['password']
            if login.check_login_info(usuario_devuelto, pass_devuelto):
                EM.util.util_values.IS_LOGIN_ACTIVE = True
                return redirect("/")
            else:
                login_form = LoginForm()
                context = {'login_form': login_form, 'Error': 'Usuario o contraseña incorrectos'}
                return render(request, 'login.html', context)