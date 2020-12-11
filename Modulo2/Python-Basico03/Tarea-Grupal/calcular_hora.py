# Calcular las horas y minutos a segundos.

def calcular_hora():
    # Recibo la hora con el metodo Input
    hora_recibida = (input("Ingrese hora del dia: "))
    # Recibo los minutos con el metodo Input
    minutos_recibidos = (input("Ingrese minutos del dia: "))
    # Chequeo que los inputs no sean nulos / pd: podria haber recibido el int
    # directamente pero no cacho bien como chequear el input parseado a int...
    if (hora_recibida != "" and minutos_recibidos != ""):
        if chequeo_de_hora(int(hora_recibida), int(minutos_recibidos)):
            # Transformo a segundos la hora
            hora_en_segundos = (int(hora_recibida) * 60) * 60
            # Transformo a segundo los minutos
            min_en_segundos = int(minutos_recibidos) * 60
            # Sumo hora y min para obtener los segundos totales
            segundos_totales = hora_en_segundos + min_en_segundos
            print("Han pasado: " + str(segundos_totales) + " desde media noche")

            if int(hora_recibida) >= 6 and int(hora_recibida) < 12:
                print("Mañana")
            elif int(hora_recibida) >= 12 and int(hora_recibida) < 17:
                print("Tarde")
            elif int(hora_recibida) >= 17 and int(hora_recibida) < 20:
                print("Atardecer")
            elif int(hora_recibida) >= 20:
                print("Noche")
            elif int(hora_recibida) >= 2 and int(hora_recibida) < 6:
                print("Madrugada")

        else:
            print("Hora no valida")
        

# Funcion que chequea que la hora sea una valida.
def chequeo_de_hora(hora, minutos):
    return False if hora > 23 or minutos > 59 else True

if __name__ == "__main__":
    calcular_hora()