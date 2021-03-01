from django.shortcuts import render
from grupal2 import settings
from .forms import FormularioContacto
from .scripts import jsonManager
import csv

# Create your views here.

def principal():
    ruta = '/app_grupal2/static/app_grupal2/data/verduras.csv'
    with open(str(settings.BASE_DIR)+ruta, 'r') as file:
        archivo =  csv.DictReader(file)
        lista = []
        for elemento in archivo:
            # Transformo el resultado a una lista para que 
            # la lectura de datos sea mas facil
            result = [elemento['Duraznos'], elemento['1990']]
            lista.append(result)
        #print(lista)
        context = {'valor': lista}
    return context

def contacto(request):
    
    if request.method == "GET":
        formulario_contacto = FormularioContacto()
        context = {'formulario_contacto': formulario_contacto}
        context.update(principal())
        return render(request, 'app_grupal2/index.html', context)

    elif request.method == "POST":
        # obtengo el formulario cuando se detecta un POST
        formulario_devuelto = FormularioContacto(request.POST)

        # Valido la informacion del formulario.
        if formulario_devuelto.is_valid():
            # Obtengo los datos ingresados por el formulario.
            datos_formulario = formulario_devuelto.cleaned_data
            # Obtengo los datos del diccionario de contacto
            diccionario_de_contactos = jsonManager.check_contacto_json()
            # Sumo 1 a la cantidad de contactos totales agregados
            nuevo_cantidad_contacto = diccionario_de_contactos['total_contactos'] + 1
            nombre_contacto = datos_formulario['nombre']
            email_contacto = datos_formulario['email']
            mensaje_contacto = datos_formulario['mensaje']

            # Creo un nombre para la key del diccionario y agrego sus valores.
            item_nuevo = 'contacto_' + str(nuevo_cantidad_contacto)
            diccionario_de_contactos[item_nuevo] = {
                "nombre": nombre_contacto,
                "email": email_contacto,
                "mensaje": mensaje_contacto
            }
            # Asigno el nuevo valor a total de contactos.
            diccionario_de_contactos['total_contactos'] = nuevo_cantidad_contacto
            # Guardo en el json los nuevos datos adquiridos
            jsonManager.guardar_contactos(diccionario_de_contactos)

            # Creo nuevamente el formulario de contacto para que la pagina no sufra cambios.
            formulario_contacto = FormularioContacto()
            context = {'formulario_contacto': formulario_contacto}
            # imprimo nuevamente las frutas del lider
            context.update(principal())
            # Y agrego en caso de querer utilizarlos los contactos ya creados.
            context.update(diccionario_de_contactos)
            return render(request, 'app_grupal2/index.html', context)
        else:
            # En caso de que el formulario venga con errores se devuelve el mismo formulario
            # pero marcando los lugares donde el usuario se equivoco.
            context = {'formulario_contacto': formulario_devuelto}
            return render(request, 'app_grupal2/index.html', context)

