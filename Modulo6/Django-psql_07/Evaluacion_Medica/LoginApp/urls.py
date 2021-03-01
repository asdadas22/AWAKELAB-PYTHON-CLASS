from django.urls import path
from . import views

app_name = 'LoginApp'

urlpatterns = [
    path('', views.login_view, name='LoginApp')
]