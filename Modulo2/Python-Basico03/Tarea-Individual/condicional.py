# Creo una lista con las preguntas:
lista_preguntas =  ["¿10 es mayor que 23? v/f: ", "¿-10 es mayor que -15? v/f: ", 
                    "¿-15 es mayor que -5? v/f: ", "¿2*5 es menor que 3? v/f: ",
                    "¿5*9 es menor que 4*12? v/f: ", "¿36/4 es menor que 48/8? v/f: ",
                    "¿El resultado de 2^5 es 32? v/f: ", 
                    "¿El perimetro de un cuadrado se calcula sumando todos sus lados? v/f: ",
                    "¿Python es 'case-Sensitivity' esto"
                     + "significa que el codigo se ejecuta linea a linea? v/f: "]

lista_respuestas = ["f", "v", "f", "f", "v", "f", "v", "v", "f"]


def crear_preguntas():
    # Condicionales por input
    print("Responda v si su respuesta es verdadera o f si su respuesta es falsa.")

    # Leo el contenido de la lista para hacer la pregunta mediante input.
    for index, pregunta in enumerate(lista_preguntas):
        result_01 = input(pregunta)
        # Como se la cantidad de preguntas que hay en la lista de preguntas
        # puedo asumir que la lista de respuestas tiene la misma cantidad de
        # items por lo tanto no necesito hacer un for exclusivo para ella.
        if result_01 != 'f' and result_01 != 'v':
            print("porfavor ingrese un caracter valido: v o f")
        elif result_01 == lista_respuestas[index]:
            print("su respuesta es correta: " + pregunta + lista_respuestas[index])
        else:
            print("su respuesta es incorrecta: " + pregunta + lista_respuestas[index])

# lista para chquear

lista_chequeo = [1, 2, 3, 6, 7, 8, 12, 13, 15, 23, 27, 33, 35, 40, 50]

def chequeo_en_lista():
    # Creo un for para hacer la pregunta varias veces.
    for n in range(0, 10):
        print("Chequee si un numero del 1 al 50 se encuentra en esta lista: ")
        # Obtengo el numero obtenido por el usuario
        parametro_a_chequear_01 = int(input("introduzca su numero entero: "))
        # chequeo si el numero que me pasan es positivo.
        if parametro_a_chequear_01 >= 0:
            # En la siguiente linea chequeo de manera sencilla si el numero
            # existe o no dentro de la lista_chequeo
            result = parametro_a_chequear_01 in lista_chequeo
            if result:
                print("El numero " + str(parametro_a_chequear_01) + " Existe en la lista")
            else:
                print("El numero " + str(parametro_a_chequear_01) + " No existe en la lista")
                    


if __name__ == "__main__":
    crear_preguntas()
    chequeo_en_lista()
