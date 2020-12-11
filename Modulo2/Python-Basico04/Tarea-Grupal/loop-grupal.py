# funcion para leer numeros y prevenir que no se repitan
def lista_no_repetida():
    # lista pelada para guardar los numeros.
    number_list = []
    # condicional que controla la cantidad de numeros qgregados a la lista
    number_count = 0
    # cantidad maxima de numeros requeridos al usuario.
    max_number_required = 15
    print("Ingrese 15 numeros a la lista")
    while (max_number_required >= number_count):
        number = input("Ingrese un numero: ")
        if number != "":
            if int(number) in number_list:
                print("El numero ya se encuentra en la lista. Intentelo nuevamente")
                continue
            else:
                number_list.append(int(number))
                number_count += 1
        else:
            print("Numero o caracter no valido. porfavor intentelo denuevo")
    
    print(number_list)


# Funcion para crear una lista de solo numeros primos

def numeros_primos():
    lista_numero_primo = []

    # Creacion de la lista con numeros del 2 al 500
    for n in range(2, 500):
        lista_numero_primo.append(n)

    # Sacando los numeros pares de la lista
    for numero in range(17, 500):
        if (numero % 2) == 0 or (numero % 3) == 0 or (numero % 5) == 0 or (numero % 7) == 0 or (numero % 11) == 0 or (numero % 13) == 0 or (numero % 17) == 0:
            lista_numero_primo.remove(numero)
    
    print(lista_numero_primo)


if __name__ == "__main__":
    # lista_no_repetida()
    numeros_primos()