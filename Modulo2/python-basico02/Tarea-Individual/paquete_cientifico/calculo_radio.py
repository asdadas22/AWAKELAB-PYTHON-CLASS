# calcular el volumen de una esfera
pi = 3.1415

def volumen_esfera():
    radio = int(input("Ingrese el radio de la esfera: "))
    if radio > 0:
        radio_al_cubo = pow(radio, 3)
        return "El volumen de la esfera es: {:.4f}".format((4 * pi * radio_al_cubo) / 3)