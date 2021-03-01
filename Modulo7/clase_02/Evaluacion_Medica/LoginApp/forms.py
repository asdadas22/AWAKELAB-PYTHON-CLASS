from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .script import login


class LoginForm(forms.Form):
    usuario = forms.CharField(
        label = 'Usuario',
        widget = forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'ingrese usuario'}),
        validators = [
                        validators.MinLengthValidator( 4, 
                            "Usuario debe tener minimo 4 caracteres")])

    password = forms.CharField(
        label = 'Password', 
        widget = forms.PasswordInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'type': 'password', 'placeholder': 'ingrese contraseña'}),
        validators = [
                        validators.MinLengthValidator( 4, 
                            "password debe tener minimo 4 caracteres")]) 