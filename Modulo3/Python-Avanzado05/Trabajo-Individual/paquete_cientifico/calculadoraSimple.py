from .exceptionEjercicio import ErrorFormula

def calculadora_simple():
    while True:
        valor_obtenido = input("Ingrese una operacion para calcular. \n" \
                                    "Por ejemplo 1 + 1:")
        valor_spliteado = str.split(valor_obtenido)
        try:
            if (valor_obtenido == "salir" or valor_obtenido == "Salir"):
                break
            elif len(valor_spliteado) > 3:
                raise ErrorFormula("El valor '{}' obtenido no es valido intentelo nuevamente.".format(valor_obtenido))
            elif valor_spliteado[1] != "+" and valor_spliteado[1] != "-":
                raise ErrorFormula("El operador '{}' obtenido no es valido intentelo nuevamente.".format(valor_spliteado[1]))
            else:
                valor_1 = float(valor_spliteado[0])
                valor_2 = float(valor_spliteado[2])
                lista_float = [valor_1, valor_2]
                if valor_spliteado[1] == "+":
                    print("El valor sumado es: %s" % (str(sum(lista_float))))
                else:
                    print("El valor restado es: %s" % (str(-sum(lista_float))))
                lista_float.clear()
        except ErrorFormula as e:
            print(e)
            continue
