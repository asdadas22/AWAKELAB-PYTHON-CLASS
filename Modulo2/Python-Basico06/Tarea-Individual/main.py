import paquete_cientifico as pc



def loopInfinito():
    while True:
        if  pc.pregunta_usuario() == False:
            break


if __name__ == "__main__":
    loopInfinito()