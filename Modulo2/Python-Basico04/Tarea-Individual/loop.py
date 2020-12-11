# Funcion para crear una pizza
def creacion_pizza():
    ingredientes_list = []

    print("Ingrese la cantidad que necesite a su pizza. \n"
     + "Para terminar la operacion escriba 'quit.'")
    while True:
        ingrediente_str = input("Ingrese un ingrediente a su pizza: ")
        if ingrediente_str != "quit":
            ingredientes_list.append(ingrediente_str)
            print("Se a agregado: " + ingrediente_str + " a la pizza")
        elif ingrediente_str == "quit":
            if len(ingredientes_list) <= 0:
                print("Pizza no valida")
            break
    
    for ingrediente in ingredientes_list:
        print("Su pizza tiene: " + ingrediente)


# Funcion para saber el precio de las entrada de cine
# de acuerdo a la edad

# Personas que estan consultando por el precio
cantidad_personas = 5

# lista para los precios / pd: esto no es necesario. simplemente
# lo hago para que quede mas generico y bonito.
lista_precio = ["Gratuita", 5000, 7000]

def entradas_cine():
    print("Cine Wark. Ticketeria")
    for n in range(0, cantidad_personas):
        edad = input("Ingrese su edad para consultar el precio del ticket: ")
        if edad != "" and int(edad) >= 0:
            if int(edad) >= 0 and int(edad) < 3:
                print("El precio de su entrada es: " + lista_precio[0])
            elif int(edad) >= 3 and int(edad) < 12:
                print("El precio de su entrada es: $" + str(lista_precio[1]))
            else:
                print("El precio de su entrada es: $" + str(lista_precio[2]))
        else:
            print("El texto ingresado no es valido intentelo nuevamente")


# Funcion para crear una pizza con ingredientes limitados
def creacion_pizza_limitada():
    ingredientes_count = 3
    ingredientes_list = []

    print("Ingrese los " + str(ingredientes_count) + " que quiere en su pizza.")
    while ingredientes_count > 0:
        ingrediente_str = input("Ingrese un ingrediente a su pizza: ")
        # append me permite agregar un item a la lista
        if ingrediente_str != "":
            ingredientes_list.append(ingrediente_str)
            print("Se a agregado: " + ingrediente_str + " a la pizza")
            ingredientes_count -= 1
        else:
            print("Pizza no valida")
            break
    
    for ingrediente in ingredientes_list:
        print("Su pizza tiene: " + ingrediente)

if __name__ == "__main__":
    # creacion_pizza()
    #entradas_cine()
    creacion_pizza_limitada()
