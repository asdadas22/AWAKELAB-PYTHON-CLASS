# funcuncion para ver los sandwiches listos

def sandwiches():
    ordenes_de_sandwiches = ["Sanwich con atun", "Sandwich con palta", "Sandwich con pollo",
                            "Sandwich con palta", "Sandwich con atun", "Barros luco", 
                            "Sandwich con carne", "Barros luco", "Sandwich con tomate", 
                            "Sandwich con hamburguesa", "Sandwich con vegano", "Barros luco",
                            "Sandwich con pollo", "Sandwich con carne", "Sandwich con palta"]
    sandwiches_terminados = []

    print("El local se ha quedado sin 'barros luco'")

    count_barros_luco = 0
    # Chequeando si existen barros lucos en la lista de ordenes
    for n in ordenes_de_sandwiches:
        if n == "Barros luco":
            count_barros_luco += 1
        
    if count_barros_luco >= 3:
        print("Existen "+ str(count_barros_luco) + " barros luco")

    # recorro la lista de ordenes para marcarlos como terminados.
    for sandwiches in ordenes_de_sandwiches:
        if(sandwiches != "Barros luco"):
            print("Su " + sandwiches + " esta terminado")
            sandwiches_terminados.append(sandwiches)

    barros_luco_list = ["Barros luco"]

    # Se declara i el cual recibe el valor que se encuentra en ordenes_de_sandwiches
    # para posterior mente evaluar si esta en la lista con los valores que quiero eliminar.
    # esto de cierto modo igual es un parche re challa. ya que tendria que agregar X
    # cantidad de items a la lista que removera a la lista principal.
    ordenes_de_sandwiches = [ i for i in ordenes_de_sandwiches if i not in barros_luco_list]

    print(sandwiches_terminados)
    print( " -------------------------- ")
    print(ordenes_de_sandwiches)


if __name__ == "__main__":
    sandwiches()
