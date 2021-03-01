import datetime

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("1900-12-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Fecha invalida")


class FormularioPaciente(forms.Form): 
    rut = forms.CharField(validators = [ 
                        validators.MinLengthValidator( 1, 
						    "rut invalido no puede ser menor a 1"),
                        validators.MaxLengthValidator( 15, 
						    "rut invalido no puede ser mayot a 99.999.999-9") ])
    nombre = forms.CharField(
                validators = [ 
                        validators.MinLengthValidator( 1, 
						    "El nombre no puede tener menos de 1 letra"),
                        validators.MaxLengthValidator( 50, 
						    "El nombre no puede tener mas de 50 letras") ])  
    edad = forms.IntegerField(validators = [ 
                        validators.MinValueValidator( 0, 
						    "No pueden ser menos de 0 años"),
                        validators.MaxValueValidator( 120, 
						    "No pueden ser más de 120 años") ])
    fecha_nacimiento = forms.DateField(validators = [validar_fecha])
    

class FormularioBusquedaPAciente(forms.Form):
    rut = forms.CharField()