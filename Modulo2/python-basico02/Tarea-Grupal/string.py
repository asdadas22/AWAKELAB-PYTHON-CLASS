import random
import math

caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz­_'
lista = []

# creo una variable para el rango del primer for para tener
# mayor control.
rango_maximo = 10

# variable que contiene el promedio del largo de los string en la lista
total_largo_promedio = 0

# Lista para ver el largo de cada lista de strings
largo_lista_string = []

for n in range(0,rango_maximo):
    string_aleatorio = ''
    largo = random.randint(1, 10)
    largo_lista_string.append(largo)
    for i in range(0, largo):
        string_aleatorio += random.choice(caracteres)
        lista.append(string_aleatorio) 
print(lista)

# Recorro la lista para sumar el valor del contenido y asi obtener poder calcular
# el promedio
for largo in largo_lista_string:
    total_largo_promedio += largo

# Promedio
promedio = math.trunc(total_largo_promedio / rango_maximo)
print(largo_lista_string)
# promedio sin truncar
print("El promedio es: " + str(promedio))
# promedio truncado
print("El promedio truncado es: " + str(math.trunc(promedio)))

for n in range(0, rango_maximo):
    for index, valorLista in enumerate(lista):
        string_aleatorio = ""
        while(len(valorLista) < math.trunc(promedio)):
            string_aleatorio += random.choice(caracteres)
            valorLista += string_aleatorio
            string_aleatorio = ""
        while(len(valorLista) > math.trunc(promedio)):
            valorLista = valorLista[:-1]
        if len(valorLista) == math.trunc(promedio):
                lista[index] = valorLista

# Imprimo la lista con con los string de largo = al promedio.
print(lista)
