from django.db import models

# Create your models here.



class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    departamentos = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    escuela = models.CharField(max_length=20)
    fecha_de_contratacion = models.DateField()
    sueldo = models.IntegerField()

class Transportista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    escuela = models.CharField(max_length=20)

    profesor = models.ManyToManyField(Profesor)
    transportista = models.ForeignKey(Transportista, on_delete=models.SET_NULL, null=True)


    