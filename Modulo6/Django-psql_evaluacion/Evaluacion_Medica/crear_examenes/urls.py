from django.urls import path
from . import views

app_name = 'crear_examenes'

urlpatterns = [
    path('', views.crear_examenes, name='crear_examenes'),
    path('grafico/', views.grafico, name='grafico'),
    path('<id>/actualizar_examen', views.editar_examen , name='actualizar_examen'),
]