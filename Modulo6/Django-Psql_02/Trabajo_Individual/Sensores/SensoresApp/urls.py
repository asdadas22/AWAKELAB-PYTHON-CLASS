from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'SensoresApp'

urlpatterns = [
    path('', views.sensor_temperatura, name='SensoresApp'),
    path('gasolina/', views.sensor_gasolina, name='SensoresApp'),
    path('puerta/', views.sensor_puerta_bodega, name='SensoresApp'),
    path('acceso/', views.sensor_acceso, name='SensoresApp'),
]