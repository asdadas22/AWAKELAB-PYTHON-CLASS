from django.urls import path
from . import views

app_name = "individual_app"

urlpatterns = [
    path('', views.departamentos, name='departamentos')
]