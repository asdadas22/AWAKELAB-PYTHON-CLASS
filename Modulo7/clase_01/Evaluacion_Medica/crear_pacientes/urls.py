from django.urls import path
from . import views

# Me sirve para llamar a las URLS en el HTML
app_name = "crear_pacientes"

urlpatterns = [
    path('', views.crear_pacientes, name='crear_pacientes'),
    path('listar_pacientes', views.listar_pacientes, name='listar_pacientes'),
    path('perfil_paciente', views.perfil_paciente, name='perfil_paciente'),
    path('<rut>/eliminar_paciente', views.eliminar_paciente, name='eliminar_paciente'),
    path('<rut>/actualizar_paciente', views.editar_paciente , name='actualizar_paciente'),
]