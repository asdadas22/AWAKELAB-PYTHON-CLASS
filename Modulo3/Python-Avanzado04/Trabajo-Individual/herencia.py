class Cuenta():

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrarDatos(self):
        return "El titular es %s y la cantidad es %s" % (self.titular, self.cantidad)

class CajaAhorro(Cuenta):

    def __init__(self, titular, cantidad):
        Cuenta.__init__(self, titular, cantidad)

class PlazoFijo(Cuenta):

    def __init__(self, titular, cantidad, plazo, interes):

        Cuenta.__init__(self, titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def importe_interes(self):
        return self.cantidad * self.interes / 100

    def mostrarDatos(self):
        return "El titular plazo: %s %s el interes es: %s total interes: %s" \
             % (self.titular, self.plazo, self.interes, str(self.importe_interes()))



if __name__ == "__main__":
    plazo_fijo_01 = PlazoFijo("Ruben", 500000, "Fijo", 20)
    print(plazo_fijo_01.mostrarDatos())

    caja_ahorro_01 = CajaAhorro("Juan", 600000)
    print(caja_ahorro_01.mostrarDatos())