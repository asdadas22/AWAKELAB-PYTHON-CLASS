from django.shortcuts import render
from .models import Asignatura, Departamento, Profesor

# Create your views here.



def asignatura(request):
    Departamento.objects.create(
                        nombre = 'Departamento de Ciencias',
                        descripcion = 'Este es el departamento de Ciencias',
                        )
    departamento_lista = Departamento.objects.all().values()

    Asignatura.objects.create(
                        nombre = 'Ciencias Sociales',
                        descripcion = 'Esta es la asignatura de Ciencias Sociales',
                        departamentos = Departamento.objects.filter(id=1)[0]
                        )
    asignatura_lista = Asignatura.objects.all().values()
   
    Profesor.objects.create(
                        nombre = 'Gilbert',
                        apellido = 'Lagos',
                        escuela = 'D822',
                        fecha_de_contratacion = '2021-01-02',
                        sueldo = 15000000
                       )
    profesor_lista = Profesor.objects.all().values()


    context =  {'asignatura_lista':asignatura_lista, 'profesor_lista':profesor_lista, 'departamento_lista':departamento_lista}
    return render(request, 'app_individual4m6/asignatura.html', context)