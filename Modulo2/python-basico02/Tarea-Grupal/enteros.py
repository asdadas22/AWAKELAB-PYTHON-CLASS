import random
import math

lista = []

# creo una variable para el rango del primer for para tener
# mayor control.
rango_maximo = 10

# variable que contiene el promedio del largo de los enteros en la lista
total_largo_promedio = 0

for n in range(0,rango_maximo):
    largo = random.randint(1, 10)
    for i in range(0, largo):
        entero_aleatorio = random.randint(1, 20)
        lista.append(entero_aleatorio) 
print(lista)

for valor in lista:
    total_largo_promedio += valor


# Promedio
promedio = math.trunc(total_largo_promedio / rango_maximo)
# promedio sin truncar
print("El promedio es: " + str(promedio))

# Restandole el promedio a los valores de la lista
for index, valor in enumerate(lista):
    lista[index] = valor - promedio

print (lista)