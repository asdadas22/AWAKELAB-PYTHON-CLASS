'''
Esta fue la unica manera que encontre de forzar un stopIteration.
No se como ocuparlo en el programa actual para hacerlo que funcione.
test_lista = [1, 2, 3]
    try:
        i = iter(test_lista)
        i.__next__()
        i.__next__()
        i.__next__()
        i.__next__()
    except Exception as ex:
        print(type(ex).__name__, ex)


//////////////////////////////////////////////////////////////////////
Con el siguiente trozo de codigo fuerzo la exception de AttributeError
ya que la variable "a" en condominio_1.a no existe

condominio_1 = pc.Condominio("Jardines", "Pedro mont", "Juanito", 40)
    try:
        print(condominio_1.a)
    except Exception as ex:
        print(type(ex).__name__, ex)

//////////////////////////////////////////////////////////////////////
En la siguiente linea de codigo se gatilla un syntaxError porque
la estructura del while esta mal realizada ya que le falta ":"
despues del True

while True print('Hello world')

'''