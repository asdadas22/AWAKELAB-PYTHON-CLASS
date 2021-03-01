from django.urls import path
from . import views

app_name = 'app_grupal2'

urlpatterns = [
    path('', views.contacto, name='formulario_contacto')
]