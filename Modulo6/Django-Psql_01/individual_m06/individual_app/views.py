from django.shortcuts import render
from .models import *

# Create your views here.

def departamentos(request):
    departamentos_recibidos = departamento.objects.values()
    print(departamentos_recibidos)
    context = {'departamentos': departamentos_recibidos}
    return render(request, 'departamentos.html', context)