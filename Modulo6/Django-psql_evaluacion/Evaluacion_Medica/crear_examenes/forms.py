from crear_pacientes.models import Paciente
from django.forms import fields
from crear_examenes.models import Examen
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import datetime


def validar_fecha(fecha):
    fecha_menor = datetime.datetime.strptime("2010-01-01", "%Y-%m-%d").date()
    fecha_mayor = datetime.datetime.strptime("2021-02-10", "%Y-%m-%d").date()
    if fecha_menor <= fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Acepta fechas entre Enero 2010 a la fecha de hoy")

class PropertyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.rut

class Examenes(forms.Form):

    # MAGIA....
    type_choices = [(i['rut'], i['rut']) for i in Paciente.objects.values('rut').distinct()]
    rut_select = forms.ChoiceField(choices=type_choices)
    
    #rut_select = forms.ModelChoiceField(queryset=Paciente.objects.all(), required=False)

    fecha = forms.DateField(validators = [validar_fecha])
    hemograma = forms.IntegerField(validators = [ 
                        validators.MinValueValidator( 100, 
						    "No pueden ser menos de 100 mg/dl"),
                        validators.MaxValueValidator( 300, 
						    "No pueden ser más de 300 mg/dl") ])
    orina = forms.IntegerField(validators = [ 
                        validators.MinValueValidator( 100, 
						    "No puede ser menos de 100 mg/dl"),
                        validators.MaxValueValidator( 300, 
						    "No puede ser más de 300 mg/dl") ])
    colesterol = forms.IntegerField(validators = [ 
                        validators.MinValueValidator( 100, 
						    "No puede ser menos de 100 mg/dl"),
                        validators.MaxValueValidator( 300, 
						    "No puede ser más de 300 mg/dl") ])
    glucosa = forms.IntegerField(validators = [ 
                        validators.MinValueValidator( 100, 
						    "No puede ser menos de 100 mg/dl"),
                        validators.MaxValueValidator( 300, 
						    "No puede ser más de 300 mg/dl") ])

class FormularioBusquedaPaciente(forms.Form):
    rut = forms.CharField()


    


