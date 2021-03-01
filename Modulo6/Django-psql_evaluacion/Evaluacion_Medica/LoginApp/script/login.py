import string
import io
import os
import json
from django.conf import settings

# Funcion para obtener los datos del json.
def check_login_info(usuario, password):
    filename= "/LoginApp/data/login_info.json"
    a_file = open(str(settings.BASE_DIR)+filename, "r")
    try:
        a_file = open(str(settings.BASE_DIR)+filename, "r")

        json_object = json.load(a_file)

        a_file.close()

        if json_object['usuario'] == usuario and json_object['password'] == password:
            return True
        else:
            return False
    except FileNotFoundError as ex:
        print(type(ex).__name__, ex)