import string
import io
import os
import json
from django.conf import settings

def check_contacto_json():
    try:
        filename= "/app_grupal2/data/registro_contacto.json"
        if os.path.isfile(str(settings.BASE_DIR)+filename) and os.access(str(settings.BASE_DIR)+"/app_grupal2/data/", os.R_OK):
            # checks if file exists
            print ("File exists and is readable")
        else:
            print ("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(str(settings.BASE_DIR)+"/app_grupal2/data/", 'registro_contacto.json'), 'w') as db_file:
                diccionario_contacto = {
                    'total_contactos': 0
                }
                db_file.write(json.dumps(diccionario_contacto))
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

def guardar_contactos(nuevo_contacto_dic):
    filename= "/app_grupal2/data/registro_contacto.json"
    a_file = open(str(settings.BASE_DIR)+filename, "r")

    json_object = json.load(a_file)

    a_file.close()

    json_object = nuevo_contacto_dic

    a_file = open(str(settings.BASE_DIR)+filename, "w")

    json.dump(json_object, a_file)

    a_file.close()