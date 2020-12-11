import datetime

# calculo el tiempo que el cuerpo se demora en recorrer cierta distancia
def tiempo_cuerpo_velocidad(distancia, velocidad):
    return distancia / velocidad

def ejercicio_C_tarea_2():
    tiempo_extra_01 = int(60 * tiempo_cuerpo_velocidad(1, 8))
    tiempo_extra_02 = int(60 * tiempo_cuerpo_velocidad(3, 15))
    tiempo_extra_03 = int(60 * tiempo_cuerpo_velocidad(1, 10))
    # Se que esto no da mas que una hora por lo tanto obvio hacer un calculo
    # que agregue horas a mi tiempo extra.
    tiempo_extra = tiempo_extra_01 + tiempo_extra_02 + tiempo_extra_03

    tiempo_base = datetime.timedelta(hours=6, minutes=52)
    tiempo_extra_recorrido = datetime.timedelta(hours=0, minutes=tiempo_extra)

    result = tiempo_base + tiempo_extra_recorrido
    return "Se demorara en total: " + result
    