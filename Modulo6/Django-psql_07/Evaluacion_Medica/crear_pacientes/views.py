import crear_examenes
from crear_examenes.models import Examen
import Evaluacion_Medica as EM
import json
import datetime


from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .script import jsonManager_paciente
from .forms import FormularioPaciente, FormularioBusquedaPAciente
from .models import *

# Create your views here.
def crear_pacientes(request):
    if EM.util.util_values.IS_DEBUG_ACTIVE or EM.util.util_values.IS_LOGIN_ACTIVE:
        if request.method == "GET":
            formulario_pacientes = FormularioPaciente()
            lista_pacientes = Paciente.objects.all().values()
            context = {'formulario': formulario_pacientes, 'pacientes': lista_pacientes}
            return render(request, 'agregar_paciente.html', context)

        elif request.method == "POST":
            formulario_recibido = FormularioPaciente(request.POST)
            if formulario_recibido.is_valid() == True:
                # recibo los datos del post y los paso a diccionario.
                datos_formulario = formulario_recibido.cleaned_data
                rut_recibido = datos_formulario['rut']
                nombre_recibido = datos_formulario['nombre']
                edad_recibida = datos_formulario['edad']
                fecha_recibida = datos_formulario['fecha_nacimiento'].strftime("%Y-%m-%d")

                Paciente.objects.create(rut = rut_recibido, nombre = nombre_recibido, 
                                            edad = edad_recibida, fecha_nacimiento = fecha_recibida)

                formulario_paciente = FormularioPaciente()
                lista_pacientes = Paciente.objects.all().values()
                context = {'formulario': formulario_paciente, 'pacientes': lista_pacientes}
                return render(request, 'agregar_paciente.html', context)

            else:
                context = {'formulario': formulario_recibido}
                return render(request, 'agregar_paciente.html', context)
                
    else:
        return redirect('/login')

def listar_pacientes(request):
    if EM.util.util_values.IS_DEBUG_ACTIVE or EM.util.util_values.IS_LOGIN_ACTIVE:
        pacientes_recibidos = Paciente.objects.values()
        diccionario_pacientes = {'pacientes': pacientes_recibidos}
        #diccionario_pacientes = jsonManager_paciente.check_pacientes_json()
        return render(request, 'listar_pacientes.html', diccionario_pacientes)
    else:
        return redirect('/login')

def eliminar_paciente(request, rut):
    if EM.util.util_values.IS_DEBUG_ACTIVE or EM.util.util_values.IS_LOGIN_ACTIVE:
        if request.method == "GET":
            context = {'rut': rut}
            return render(request, "eliminar_paciente.html", context)
        elif request.method == "POST":
            paciente_1 = Paciente.objects.filter(rut = rut).all()
            print(paciente_1[0].id)
            Examen.objects.filter(paciente_id = paciente_1[0].id).delete()
            paciente_1.delete()
            return redirect('/listar_pacientes')
    else:
        return redirect('/login')

def editar_paciente(request, rut):
    if request.method == "GET":
        paciente = Paciente.objects.filter(rut= rut).values()[0]
        formulario = FormularioPaciente(initial=paciente)
        context = {'formulario': formulario, 'identificador': rut}
        return render(request, 'actualizar_paciente.html', context)
    elif request.method == "POST":
        formulario_recibido = FormularioPaciente(request.POST)
        if formulario_recibido.is_valid() == True:
            # recibo los datos del post y los paso a diccionario.
            datos_formulario = formulario_recibido.cleaned_data
            rut_recibido = datos_formulario['rut']
            nombre_recibido = datos_formulario['nombre']
            edad_recibida = datos_formulario['edad']
            fecha_recibida = datos_formulario['fecha_nacimiento'].strftime("%Y-%m-%d")

            Paciente.objects.filter(rut = rut).update(rut = rut_recibido, nombre = nombre_recibido, 
                                                        edad = edad_recibida, fecha_nacimiento = fecha_recibida)
            messages.success(request, 'El paciente con rut: %s fue actualizado correctamente' % rut)
            return redirect("/listar_pacientes")


def perfil_paciente(request):
    if EM.util.util_values.IS_DEBUG_ACTIVE or EM.util.util_values.IS_LOGIN_ACTIVE:
        if request.method == "GET":
            formulario_busqueda = FormularioBusquedaPAciente()
            context = {'formulario_busqueda': formulario_busqueda}
            return render(request, 'perfil_paciente.html', context)
        elif request.method == "POST":
            formulario_recibido = FormularioBusquedaPAciente(request.POST)
            print(formulario_recibido)
            datos_recibido = formulario_recibido.cleaned_data
            rut_recibido = datos_recibido['rut']
            diccionario_pacientes = jsonManager_paciente.check_pacientes_json()
            pacientes = diccionario_pacientes['pacientes']
            for paciente in pacientes:
                if paciente['rut'] == rut_recibido:
                    formulario_busqueda = FormularioBusquedaPAciente()
                    context = {'formulario_busqueda': formulario_busqueda}
                    context.update(paciente)
                    return render(request, 'perfil_paciente.html', context)
    else:
        return redirect('/login')

