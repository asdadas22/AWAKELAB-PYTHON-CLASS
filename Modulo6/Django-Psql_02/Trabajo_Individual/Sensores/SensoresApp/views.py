from django.shortcuts import render
from .models import *

# Create your views here.

def sensor_temperatura(request):
    datos_recibidos = SensorTemperatura.objects.values()
    context = {'datos': datos_recibidos}
    return render(request, 'sensor_temperatura.html', context)

def sensor_puerta_bodega(request):
    datos_recibidos = SensorPuerta.objects.values()
    context = {'datos': datos_recibidos}
    return render(request, 'sensor_puerta.html', context)

def sensor_gasolina(request):
    datos_recibidos = SensorGasolina.objects.values()
    context = {'datos': datos_recibidos}
    return render(request, 'sensor_gasolina.html', context)

def sensor_acceso(request):
    datos_recibidos = SensorAcceso.objects.values()
    context = {'datos': datos_recibidos}
    return render(request, 'sensor_acceso.html', context)