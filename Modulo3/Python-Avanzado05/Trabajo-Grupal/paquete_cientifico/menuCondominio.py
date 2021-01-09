from .condominio import *
import time

lista_condominios = []

def print_message_menu():
    print(" --------- MENU PARA MANEJAR CONDOMINIO ---------")
    print("1- Agregar un nuevo condominio\n" \
          "2- Agregar estacionamientos\n" \
          "3- Cambiar administrador\n" \
          "4- Obtener informacion de un condominio:\n" \
          "5- Salir del programa")

def start_menu():
    print_message_menu()
    while True:
        try:
            valor_recibido = int(input("Digite la accion que necesita realizar: "))
            # resultado de la operacion ejecutada por el usuario
            result = handle_option(valor_recibido)
            if (result == -1):
                break
            # se imprimen los condominios
            elif result[1] == 1:
                for condominio in result[0]:
                    print(condominio)
                time.sleep(2)
                print_message_menu()
            # se imprime la informacion del condominio
            elif result[1] == 2:
                print(result[0])
                time.sleep(2)
                print_message_menu()
                

        except (ValueError, TypeError) as ex:
            print(type(ex).__name__, ex)
            print("intentelo nuevamente...")
            print_message_menu()
            continue


def handle_option(valor_recibido):
    if valor_recibido == 5:
        return -1
    elif valor_recibido == 1:
        try:
            while True:
                nombre_recibido = input("Ingrese el nombre de condominio: ")
                direccion_recibida = input("Ingrese la direccion del condominio: ")
                administrador_recibido = input("Ingrese el administrador del condominio: ")
                num_estacionamiento_recibida = int(input("Ingrese la direccion del condominio: "))
                if (nombre_recibido == "" or direccion_recibida == "" 
                    or administrador_recibido == "" or num_estacionamiento_recibida == ""):
                    print("Todos los cambios son obligatorios intentelo nuevamente.")
                    continue
                else:
                    break
            condominio_01 = Condominio(nombre_recibido, direccion_recibida, 
                                administrador_recibido, num_estacionamiento_recibida)
            lista_condominios.append(condominio_01)
            return [lista_condominios, 1]
        except ValueError as ex:
            print(type(ex).__name__, ex)

    elif valor_recibido == 4:
        indice_recibido = int(input("Ingrese un indice para buscar el condominio: "))
        return get_info_condominio_by_index(indice_recibido)


def get_info_condominio_by_index(index):
    try:
        return [lista_condominios[index], 2]
    except LookupError as ex:
        print(type(ex).__name__, ex)
        
    