'''
Aca tengo un setter. esto con el fin de modificar tanto la variable
y alguna otra que dependa de esta misma.

@property
def color(self):
    return self.__color

@color.setter
def color(self, color_nuevo):
    self.__color = color_nuevo
'''


class Condominio():

    def __init__(self, direccion, lista_administrador, lista_guardias, 
                num_unidades_habitacionales, lista_unidades, cuenta_corriente,
                num_quincho, num_piscina, num_estacionamiento, num_basureros, nombre_administrador):
        self.direccion = direccion
        self.lista_administrador = lista_administrador
        self.lista_guardias = lista_guardias
        self.num_unidades_habitacionales = num_unidades_habitacionales
        self.lista_unidades = lista_unidades
        self.__cuenta_corriente = cuenta_corriente

        self.num_quincho = num_quincho
        self.num_piscina = num_piscina
        self.num_estacionamiento = num_estacionamiento
        self.num_basureros = num_basureros

        self.guardia = Guardia("Ruben", 25, "Hola@gmail.com")
        self.unidad_habitacional = UnidadHabitacional(100, 6, 2, 4)
        self.nuevo_administrador = nombre_administrador


    def get_direccion(self):
        return self.direccion

    def set_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        return self.direccion

    def set_administrador(self):
        pass

    def get_administrador(self):
        return self.nuevo_administrador

    def add_guardia(self):
        pass

    def del_guardia(self):
        pass

    def get_guardias(self):
        return self.lista_guardias

    def get_unidades(self):
        return self.unidad_habitacional.get_tamanio_unidad()

    def get_num_quinchos(self):
        return self.num_quincho

    def get_guardia(self):
        return self.guardia.get_guardia_info()

    def get_num_estacionamientos(self):
        return self.num_estacionamiento


class Terrenos():

    def __init__(self, num_casas, tamanio_cuadrado, tipo_suelo):
        self.num_casas = num_casas
        self.tamanio_cuadrado = tamanio_cuadrado
        self.tipo_suelo = tipo_suelo

    def get_tamanio(self):
        return self.tamanio_cuadrado

    def set_num_casas(self, nuevo_numero):
        self.num_casas = nuevo_numero
        return self.num_casas

    def get_terreno_info(self):
        return "El numero de casas maximo es: %s \n"\
                "El tamaño cuadrado es: %s \n"\
                "El tipo de suelo es: %s" % (self.num_casas, self.tamanio_cuadrado, self.tipo_suelo)

class CondominioVertical(Terrenos, Condominio):

    def __init__(self, direccion, lista_administrador, lista_guardias, 
                num_unidades_habitacionales, lista_unidades, cuenta_corriente,
                num_quincho, num_piscina, num_estacionamiento, num_basureros, 
                nombre_administrador, num_casas, tamanio_cuadrado, tipo_suelo, 
                nombre_condominio, num_grifos, linea_directa):
                Terrenos.__init__(self, num_casas, tamanio_cuadrado, tipo_suelo)
                Condominio.__init__(self, direccion, lista_administrador, lista_guardias, 
                num_unidades_habitacionales, lista_unidades, cuenta_corriente,
                num_quincho, num_piscina, num_estacionamiento, num_basureros, nombre_administrador)

                self.nombre_condominio = nombre_condominio
                self.num_grifos = num_grifos
                self.linea_directa = linea_directa

    def condominio_vertical_info(self):
        return "Direccion: %s - nombre condominio: %s \n"\
                "numero estacionamientos: %s - tamaño cuadrado del terreno: %s "\
                % (self.direccion, self.nombre_condominio, self.num_estacionamiento, self.tamanio_cuadrado)


    # Polimorfimos. esta funcion se sobre escribe para que funcione distinto que en su padre.
    def set_administrador(self, nuevo_administrador):
        self.nuevo_administrador = nuevo_administrador
        return self.nuevo_administrador



class Guardia():

    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def get_email(self):
        return self.email

    def get_guardia_info(self):
        return "El nombre del guardia es: %s \nsu edad es: %s \n" \
            "Su email es: %s" % (self.nombre, self.edad, self.email)

    def change_email(self, nuevo_email):
        self.email = nuevo_email
        return self.email

    def add_edad(self):
        self.edad += 1
        return self.edad


class UnidadHabitacional():

    def __init__(self, tamanio, num_ventanas, num_baños, num_piezas):
        self.tamanio = tamanio
        self.num_ventanas = num_ventanas
        self.num_baños = num_baños
        self.num_piezas = num_piezas

    def get_tamanio_unidad(self):
        return self.tamanio

    def get_num_ventana(self):
        return self.num_ventanas

    def get_num_baños(self):
        return self.num_baños

    def get_num_piezas(self):
        return self.num_piezas

