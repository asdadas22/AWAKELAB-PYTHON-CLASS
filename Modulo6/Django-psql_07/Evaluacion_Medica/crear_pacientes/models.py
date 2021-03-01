from django.db import models

from crear_examenes import models as examenes_model

# Create your models here.

class Paciente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()