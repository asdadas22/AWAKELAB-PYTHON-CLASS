from django.shortcuts import render
from .models import Alumno, Asignatura, Departamento, Profesor, Transportista

# Create your views here.



def asignatura(request):
    departamento_lista = Departamento.objects.all().values()

    asignatura_lista = Asignatura.objects.all().values()
   
    profesor_lista = Profesor.objects.all().values()

    lista_alumnos = Alumno.objects.all()
    lista_transportista = Transportista.objects.all()


    context =  {'asignatura_lista':asignatura_lista, 
                'profesor_lista':profesor_lista, 
                'departamento_lista':departamento_lista,
                'lista_alumnos': lista_alumnos,
                'lista_transportista': lista_transportista}
    return render(request, 'app_individual4m6/asignatura.html', context)