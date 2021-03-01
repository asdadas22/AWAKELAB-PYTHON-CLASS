import string
import io
import os
import json
from django.conf import settings

def check_paciente_especifico_json():
    try:
        filename= "/Evaluacion_Medica/data/datos_pacientes.json"
        if os.path.isfile(str(settings.BASE_DIR)+filename) and os.access(str(settings.BASE_DIR)+"/Evaluacion_Medica/data/", os.R_OK):
            # checks if file exists
            print ("File exists and is readable")
            return get_json_info(str(settings.BASE_DIR)+filename)
        else:
            print ("Either file is missing or is not readable, please create a new patient to add exam...")
            return False
    except Exception as ex:
        print(type(ex).__name__, ex)

# Funcion para obtener los datos del json.
def get_json_info(pathJson):
    try:
        a_file = open(pathJson, "r")

        json_object = json.load(a_file)

        a_file.close()
        return json_object
    except FileNotFoundError as ex:
        print(type(ex).__name__, ex)

def guardar_examenes(nuevo_examen):
    filename= "/Evaluacion_Medica/data/datos_pacientes.json"
    a_file = open(str(settings.BASE_DIR)+filename, "r")

    json_object = json.load(a_file)

    a_file.close()

    json_object = nuevo_examen

    a_file = open(str(settings.BASE_DIR)+filename, "w")

    json.dump(json_object, a_file)

    a_file.close()