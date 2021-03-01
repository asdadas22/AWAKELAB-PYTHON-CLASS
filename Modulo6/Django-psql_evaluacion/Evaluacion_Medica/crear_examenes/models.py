from django.db import models
from django.db.models.fields import DateField
from crear_pacientes import models as CP_App

# Create your models here.

class Examen (models.Model):
    fecha = models.DateField()
    hemograma = models.IntegerField()
    orina = models.IntegerField()
    colesterol = models.IntegerField()
    glucosa = models.IntegerField()

    paciente = models.ForeignKey(CP_App.Paciente, on_delete=models.SET_NULL, null=True)