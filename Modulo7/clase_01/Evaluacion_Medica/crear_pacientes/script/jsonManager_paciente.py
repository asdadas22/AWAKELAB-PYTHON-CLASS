import string
import io
import os
import json
from django.conf import settings

def check_pacientes_json():
    try:
        filename= "/Evaluacion_Medica/data/datos_pacientes.json"
        if os.path.isfile(str(settings.BASE_DIR)+filename) and os.access(str(settings.BASE_DIR)+"/Evaluacion_Medica/data/", os.R_OK):
            # checks if file exists
            print ("File exists and is readable")
        else:
            print ("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(str(settings.BASE_DIR)+"/Evaluacion_Medica/data/", 'datos_pacientes.json'), 'w') as db_file:
                tmp_diccionario_paciente = {
                    'pacientes': []
                }
                db_file.write(json.dumps(tmp_diccionario_paciente))
                db_file.close()
        return get_json_info(str(settings.BASE_DIR)+filename)
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

def guardar_pacientes(nuevo_contacto_dic):
    filename= "/Evaluacion_Medica/data/datos_pacientes.json"
    a_file = open(str(settings.BASE_DIR)+filename, "r")

    json_object = json.load(a_file)

    a_file.close()

    json_object = nuevo_contacto_dic

    a_file = open(str(settings.BASE_DIR)+filename, "w")

    json.dump(json_object, a_file)

    a_file.close()