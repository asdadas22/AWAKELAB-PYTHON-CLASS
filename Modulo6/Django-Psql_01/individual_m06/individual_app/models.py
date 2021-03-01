from django.db import models

# Create your models here.

class departamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=120)