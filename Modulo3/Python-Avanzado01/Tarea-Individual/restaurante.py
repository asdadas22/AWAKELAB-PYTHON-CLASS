class Restaurante():

    numero_servicio = 0

    def __init__(self, restaurant_nombre, cocina_tipo):
        self.name = restaurant_nombre
        self.cocina_tipo = cocina_tipo

    def describre_restaurant(self):
        print("El nombre del restaurante es: " + self.name)
        print("El tipo de cocina es: " + self.cocina_tipo)

    def abrir_restaurant(self):
        print("El restaurant esta abierto")

    def set_numero_servicio(self, nuevo_numero):
        self.numero_servicio = nuevo_numero
        print("numero de servicio: " + str(self.numero_servicio))

    def incrementar_numero_servicio(self, personas_atendidas):
        self.numero_servicio += personas_atendidas
        print("El total de personas atendidas es: " + str(self.numero_servicio))





restaurante_01 = Restaurante("El guaton", "cocina rapida")
restaurante_02 = Restaurante("Navoli", "cocina piola")
restaurante_03 = Restaurante("Sushi", "comida extrangera")

restaurante_01.describre_restaurant()
restaurante_01.set_numero_servicio(10)
restaurante_01.incrementar_numero_servicio(560)
print("=============================")
restaurante_02.describre_restaurant()
print("=============================")
restaurante_03.describre_restaurant()