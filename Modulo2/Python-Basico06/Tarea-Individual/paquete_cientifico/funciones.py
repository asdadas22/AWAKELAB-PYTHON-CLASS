diccionario_de_usuarios = {
    "version": 1.0,
}

# Funcion que pregunta el nombre al usuario.


def pregunta_usuario():
    print("Si desea terminar la operacion escriba 'salir'")
    nombre = input("Ingrese su nombre porfavor: ")
    if nombre == "salir" or nombre == "Salir":
        return False
    else:
        pregunta_numero(nombre)

# Pregunta un numero entero al usuario


def pregunta_numero(nombre_usuario):
    result_factorial = 0
    contador = 0
    while True:
        try:
            valor_recibido = int(input("Ingrese un numero entero: "))
            if valor_recibido <= 0:
                print("El valor tiene que ser mayor a 0")
                continue
        except ValueError:
            print("No es un entero. Intentelo nuevamente")
            continue
        else:
            contador += 1
            result_factorial = calcular_factorial(valor_recibido)
            item_nuevo = nombre_usuario + "_" + str(contador)
            diccionario_de_usuarios[item_nuevo] = {
                "nombre": nombre_usuario,
                "entero": valor_recibido,
                "factorial": result_factorial
            }
            print(diccionario_de_usuarios)
            break


# Calcula un factorial del numero ingresado por el usuario.
def calcular_factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado
