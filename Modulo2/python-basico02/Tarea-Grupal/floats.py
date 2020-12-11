import random
import math

lista = []

# creo una variable para el rango del primer for para tener
# mayor control.
rango_maximo = 10

# variable que contiene el promedio del largo de los floats en la lista
total_largo_promedio = 0

for n in range(0,rango_maximo):
    largo = random.randint(1, 10)
    for i in range(0, largo):
        float_aleatorio = round(random.uniform(10, 50), 3)
        lista.append(float_aleatorio) 
print(lista)

# Obtengo la suma total de los valores de la lista
for valor in lista:
    total_largo_promedio += valor


# Promedio
promedio = math.trunc(total_largo_promedio / rango_maximo)
# promedio sin truncar
print("El promedio es: " + str(promedio))
# Suma total de los objetos en la lista
print(total_largo_promedio)
# Valor maximo dentro de la lista
print(max(lista))