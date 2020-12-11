import random

posiciones = {
    7: " ", 8: " ", 9: " ",
    4: " ", 5: " ", 6: " ",
    1: " ", 2: " ", 3: " " 
}

def printTablero(tablero):
    print(tablero[7] + ' | ' + tablero[8] + " | " + tablero[9])
    print("──┼───┼───")
    print(tablero[4] + ' | ' + tablero[5] + " | " + tablero[6])
    print("──┼───┼───")
    print(tablero[1] + ' | ' + tablero[2] + " | " + tablero[3])
    print("\n")


def jugadas():

    playerTurn = True
    # contador para ver cuantas jugadas van
    turn = 0
    for i in range(10):
        if playerTurn:
            # Agarro por consola la posicion del jugador.
            key_position = int(input("Cual sera tu jugada, indica una casilla del 1 al 9: "))
            # Verifico que no tenga nada la casilla donde el jugador intenta poner su ficha
            if posiciones[key_position] == " ":
                posiciones[key_position] = "X"
        else:
            rndBotPlay = random.randint(1, 9)
            while True:
                if posiciones[rndBotPlay] != " ":
                    rndBotPlay = random.randint(1, 9)
                # Verifico que no tenga nada la casilla donde el jugador intenta poner su ficha
                if posiciones[rndBotPlay] == " ":
                    posiciones[rndBotPlay] = "O"
                    break
        turn += 1

        # imprimo el tablero luego de la jugada.
        printTablero(posiciones)
                
        # Realizo el chequeo del tablero para verificar si alguien gano.
        if chequeoEstadoTablero(turn):
            if playerTurn:
                print("Felicidades has ganado en el turno:", turn)
            else:
                print("Has perdido.")
            break
        
        if playerTurn:
            playerTurn = False
        else:
            playerTurn = True


def chequeoEstadoTablero(turn):
    result = False
    # Verifico en el turno 5 las opciones de victoria.
    # ya que antes no se puede ganar.
    if turn >= 5:
        if posiciones[7] == posiciones[8] == posiciones[9] != " ":
            result = True
        elif posiciones[7] == posiciones[4] == posiciones[1] != " ":
            result = True
        elif posiciones[7] == posiciones[5] == posiciones[3] != " ":
            result = True
        elif posiciones[4] == posiciones[5] == posiciones[6] != " ":
            result = True
        elif posiciones[1] == posiciones[2] == posiciones[3] != " ":
            result = True
        elif posiciones[9] == posiciones[6] == posiciones[3] != " ":
            result = True
        elif posiciones[9] == posiciones[5] == posiciones[1] != " ":
            result = True
        elif posiciones[8] == posiciones[5] == posiciones[2] != " ":
            result = True

    return result


if __name__ == "__main__":
    print("\n NUEVA PARTIDA! GATO EXTREMO")
    printTablero(posiciones)
    jugadas()