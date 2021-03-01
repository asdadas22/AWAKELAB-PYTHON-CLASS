from django.urls import path
from . import views

app_name = 'LoginApp'

urlpatterns = [
    path('login/', views.login_view, name='LoginApp'),
    path('', views.inicio, name='inicio')
]