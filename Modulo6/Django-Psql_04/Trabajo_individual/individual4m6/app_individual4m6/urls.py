from django.urls import path
from . import views

app_name = 'app_individual4m6'

urlpatterns = [
    path('', views.asignatura, name='asignatura'),
]