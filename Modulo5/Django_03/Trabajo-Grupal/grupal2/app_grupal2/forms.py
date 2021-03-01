from django import forms
from django.core import validators
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class FormularioContacto(forms.Form):
    nombre = forms.CharField(
        validators = [
            validators.MinLengthValidator(4, "El nombre no puede ser menor a 4 letras"),
            validators.MaxLengthValidator(15, "El nombre no puede superar los 15 caracteres")   
        ]
    )
    email = forms.EmailField()

    mensaje = forms.CharField(
        widget = forms.Textarea,
        validators = [
            validators.MinLengthValidator(15, "El mensaje no puede ser menor a 15 caracteres")
        ]
    )
    forms.