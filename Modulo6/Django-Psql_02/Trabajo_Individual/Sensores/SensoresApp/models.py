from django.db import models

# Create your models here.

class SensorTemperatura(models.Model):
    nombre_sensor = models.CharField(max_length=50)
    fecha_sensada = models.DateField()

class SensorGasolina(models.Model):
    nombre_sensor = models.CharField(max_length=50)
    fecha_sensada = models.DateField()
    nivel = models.CharField(max_length=50)

class SensorPuerta(models.Model):
    nombre_sensor = models.CharField(max_length=50)
    fecha_sensada = models.DateField()

class SensorAcceso(models.Model):
    nombre_sensor = models.CharField(max_length=50)
    fecha_sensada = models.DateField()