from crear_examenes.models import Examen
from crear_pacientes import models as CP_Mod
import json

from django.shortcuts import render, redirect
from django.contrib import messages
from .script import jsonManager_examen
from .forms import Examenes, FormularioBusquedaPaciente, PropertyModelChoiceField
from django.conf import settings
import Evaluacion_Medica as EM

def crear_examenes(request):
    if EM.util.util_values.IS_DEBUG_ACTIVE or EM.util.util_values.IS_LOGIN_ACTIVE:
        if request.method == "GET":
            formulario_examenes = Examenes() 
            formulario_busqueda = FormularioBusquedaPaciente()
            # Recibo el primer paciente de la DB
            paciente_especifico = CP_Mod.Paciente.objects.all()[:1].get()
            examenes_recibidos = Examen.objects.filter(paciente_id = paciente_especifico.id).values()
            # Agregamos los datos necesarios al diccionario.
            
            context = {'formulario': formulario_examenes,
                        'formulario_busqueda': formulario_busqueda,
                        'examenes': examenes_recibidos,
                        'paciente': paciente_especifico}
            return render(request, 'registroexamenes.html', context)

        elif request.method == "POST":
            # Obtengo el formulario recibido por el post
            formulario_recibido = Examenes(request.POST)
            formulario_busqueda_recibido = FormularioBusquedaPaciente(request.POST)
            if formulario_recibido.is_valid():
                # aca transformamos los datos del formulario a diccionario
                datos_formulario = formulario_recibido.cleaned_data
                # Creas variables con los datos recibidos para mejor lectura.
                rut_recibido = datos_formulario['rut_select']
                orina_recibida = datos_formulario['orina']
                hemograma_recibido = datos_formulario['hemograma']
                fecha_recibida = datos_formulario['fecha'].strftime("%Y-%m-%d")
                colesterol_recibido = datos_formulario['colesterol']
                glucosa_recibida = datos_formulario['glucosa']
                # Busco al paciente de acuerdo al rut recibido
                paciente = CP_Mod.Paciente.objects.filter(rut = rut_recibido).values()
                # Creo el examen con la id del paciente especifico.
                Examen.objects.create(fecha = fecha_recibida, hemograma = hemograma_recibido,
                                        orina = orina_recibida, colesterol = colesterol_recibido,
                                        glucosa = glucosa_recibida, paciente_id = paciente[0]['id'])
                formulario_examenes = Examenes()
                formulario_busqueda = FormularioBusquedaPaciente()
                examenes_recibidos = Examen.objects.filter(paciente_id=paciente[0]['id']).values()
                
                context = {'formulario': formulario_examenes,
                            'examenes': examenes_recibidos,
                            'formulario_busqueda': formulario_busqueda}
                return render(request, 'registroexamenes.html', context)
            elif formulario_busqueda_recibido.is_valid():
                datos_formulario_busqueda_recibidos = formulario_busqueda_recibido.cleaned_data
                
                rut_recibido = datos_formulario_busqueda_recibidos['rut']
                paciente_especifico = CP_Mod.Paciente.objects.filter(rut=rut_recibido).values()
                print(paciente_especifico)
                if paciente_especifico:
                    examenes_recibidos = Examen.objects.filter(paciente_id = paciente_especifico[0]['id']).values()
                    
                    formulario_examenes = Examenes()
                    formulario_busqueda = FormularioBusquedaPaciente()
                    context = {'formulario': formulario_examenes, 
                                'formulario_busqueda': formulario_busqueda,
                                'examenes': examenes_recibidos,
                                'paciente': paciente_especifico[0]}
                    return render(request, 'registroexamenes.html', context)
                else:
                    messages.error(request, 'El rut: ' + rut_recibido + ' No existe. Intentelo nuevamente')
                    formulario_examenes = Examenes()
                    formulario_busqueda = FormularioBusquedaPaciente()
                    context = {'formulario': formulario_examenes,
                                'formulario_busqueda': formulario_busqueda,}
                    return render(request, 'registroexamenes.html', context)
            else:    
                formulario_examenes = Examenes()
                formulario_busqueda = FormularioBusquedaPaciente()
                context = {'formulario': formulario_examenes,
                            'formulario_busqueda': formulario_busqueda,}
                return render(request, 'registroexamenes.html', context)

        else:
            formulario_examenes = Examenes()
            context = {'formulario': formulario_examenes}
            return render(request, 'registroexamenes.html', context)
    else:
        return redirect('/login')

def editar_examen(request, id):
    if request.method == "GET":

        examen = Examen.objects.filter(id = id).values()[0]
        
        formulario = Examenes(initial=examen)
        context = {'formulario': formulario, 'identificador': examen['id']}
        return render(request, 'actualizar_examen.html', context)
    elif request.method == "POST":
            # Obtengo el formulario recibido por el post
            formulario_recibido = Examenes(request.POST)
            if formulario_recibido.is_valid():
                # aca transformamos los datos del formulario a diccionario
                datos_formulario = formulario_recibido.cleaned_data
                # Creas variables con los datos recibidos para mejor lectura.
                rut_recibido = datos_formulario['rut_select']
                orina_recibida = datos_formulario['orina']
                hemograma_recibido = datos_formulario['hemograma']
                fecha_recibida = datos_formulario['fecha'].strftime("%Y-%m-%d")
                colesterol_recibido = datos_formulario['colesterol']
                glucosa_recibida = datos_formulario['glucosa']
                # Busco al paciente de acuerdo al rut recibido
                paciente = CP_Mod.Paciente.objects.filter(rut = rut_recibido).values()
                # Creo el examen con la id del paciente especifico.
                Examen.objects.filter(id=id).update(fecha = fecha_recibida, hemograma = hemograma_recibido,
                                        orina = orina_recibida, colesterol = colesterol_recibido,
                                        glucosa = glucosa_recibida, paciente_id = paciente[0]['id'])
                
                messages.success(request, 'EL EXAMEN con ID: %s fue editado existosamente' % id)

                return redirect('/crear_examenes')
    


def grafico(request):
    if EM.util.util_values.IS_DEBUG_ACTIVE or EM.util.util_values.IS_LOGIN_ACTIVE:

        lista_orina = []
        lista_glucosa = []
        formulario_busqueda = FormularioBusquedaPaciente()
        if request.method == "GET":
            paciente_encontrado = CP_Mod.Paciente.objects.filter(id=1).values()
            examenes = Examen.objects.filter(paciente_id=1).values()
            for examen in examenes:
                lista_orina.append(examen['orina'])
                lista_glucosa.append(examen['glucosa'])

            context = {'formulario_busqueda': formulario_busqueda, 
                        'orina':lista_orina, 
                        'glucosa':lista_glucosa,
                        'paciente':paciente_encontrado[0]
                        }
            return render(request, 'graficos.html', context)
        elif request.method == "POST":
            lista_glucosa.clear()
            lista_orina.clear()
            formulario_recibido = FormularioBusquedaPaciente(request.POST)
            print(formulario_recibido)
            datos_recibidos = formulario_recibido.cleaned_data
            rut_recibido = datos_recibidos['rut']
            paciente_encontrado = CP_Mod.Paciente.objects.filter(rut = rut_recibido).values()
            examenes = Examen.objects.filter(paciente_id=paciente_encontrado[0]['id']).values()
            for examen in examenes:
                lista_orina.append(examen['orina'])
                lista_glucosa.append(examen['glucosa'])
            context = {'formulario_busqueda': formulario_busqueda, 
                        'orina':lista_orina, 
                        'glucosa':lista_glucosa,
                        'paciente':paciente_encontrado[0]
                        }
            return render(request, 'graficos.html', context)
    else:
        return redirect('/login')
