import random
import time

# Turnos restantes antes de que sea game over
lifes = 0

# esto lo copie de internet para ahorrar el trabajo.
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

palabras_random_list = ["python", "casa", "perro", "hipopotamo", "camioneta", "valparaiso"]


def obtenerPalabraAleatoria(lista_de_palabras):
    # selecciono un index random para obtener una palabra de la lista
    index_rnd = random.randint(0, len(lista_de_palabras) - 1)
    # manejo la palabra oculta.
    palabra_oculta = ocultarPalabra(lista_de_palabras[index_rnd])
    # cambio la primera letra de la palabra a 0 ya que la estoy dando de ayuda.
    tmp_palabra = list(lista_de_palabras[index_rnd])
    tmp_palabra[0] = "0"
    palabra = "".join(tmp_palabra)
    # retorno en una lista los objetos que necesito.
    result = [palabra, palabra_oculta]
    return result

# lo que hago en esta funcion es cambiar la palabra por X para que no se vea
def ocultarPalabra(palabra):
  tmp_palabra = list(palabra)
  # Saco la primera letra de la palabra.
  palabra_oculta = tmp_palabra[0]
  for i in range(1, len(palabra)):
      palabra_oculta = palabra_oculta[:i] + "X"
  return palabra_oculta

# Metodo utilizado para chequear la letra que el jugador ha ingresado.
def chequeoLetraIngresada(palabra, palabra_oculta, letra):
  # lista que guarda los indices de las letras encontradas.
  # para posteriormente agregarlas a "palabra_oculta"
  index_list = []

  exist = False
  while True:
    if palabra.find(letra) != -1:
      index_list.append(palabra.find(letra))
      tmp_palabra = list(palabra)
      # para no reformular la logica actual. lo que hice fue simplemente cambiar
      # el valor. en esta caso la letra la cambio por un 0 para que no la detecte mas.
      tmp_palabra[palabra.find(letra)] = "0"
      palabra = "".join(tmp_palabra)
      #palabra = palabra.strip(letra)
      print(palabra)
      exist = True
    else:
      break

  tmp_palabra_oculta_list = list(palabra_oculta)
  for index in index_list:
    del tmp_palabra_oculta_list[index]
    tmp_palabra_oculta_list.insert(index, letra)
    palabra_oculta = "".join(tmp_palabra_oculta_list)

  result = [exist, palabra, palabra_oculta]
  index_list.clear()
  return result
  

      
def game(tmp_lifes):
  life_dummy = 6
  # Obtengo la palabra que se utilizara para el juego
  result_palabra_rnd = obtenerPalabraAleatoria(palabras_random_list)
  palabra =  result_palabra_rnd[0]
  palabra_oculta = result_palabra_rnd[1]

  # como la palabra la estoy cambiando constantemente.
  # guardo la palabra al principio para tenerla como referencia.
  palabra_base = palabra

  while tmp_lifes <= 6:
    print(AHORCADO[tmp_lifes])
    print("\n Cheat: " + palabra)
    print("\n La palabra a adivinar es: " + palabra_oculta)
    try:
        letra = input("Ingrese una letra de la palabra a adivinar: ")
        if letra.isdigit():
            print("Solo se pueden ingresar letras. Intentelo nuevamente")
            time.sleep(2)
            continue
        elif len(letra) > 1:
            print("Solo se puede agregar una letra por turno. Intentelo nuevamente")
            time.sleep(2)
            continue
    except ValueError:
        print("Debe ingresar una letra. caracteres especiales o numeros no estan permitidos." + 
        "\n Intentelo nuevamente. ")
        time.sleep(2)
        continue

    chequeo_letra_result = chequeoLetraIngresada(palabra, palabra_oculta, letra)
    if not chequeo_letra_result[0]:
      tmp_lifes += 1
      if life_dummy - tmp_lifes <= 0:
        print(AHORCADO[6])
        print("Game over.")
        break
      else:
        print("Has perdido una vida! Te quedan: " + str(life_dummy - tmp_lifes))
        time.sleep(1.5)
        continue
    else:
      print("Has acertado ")
      palabra = chequeo_letra_result[1]
      palabra_oculta = chequeo_letra_result[2]
      if palabra_base == palabra_oculta:
        print("Felicidades has ganado")
        break
      else:
        time.sleep(1.5)
        continue


game(lifes)