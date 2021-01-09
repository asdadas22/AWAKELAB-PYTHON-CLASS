# forzando un importError
try:
    import menuCondominio
except ImportError as ex:
    print(type(ex).__name__, ex)

class Condominio():

    def __init__(self, nombre, direccion, administrador, num_estacionamientos):
        self.nombre = nombre
        self.direccion = direccion
        self.administrador = administrador
        self.num_estacionamientos = num_estacionamientos

    def __str__(self):
        return "Nombre: %s Direccion: %s Administrador: %s num_estacionamiento: %s" \
                % (self.nombre, self.direccion, self.administrador, self.num_estacionamientos)

    def cambiar_administrador(self, nuevo_admin):
        self.administrador = nuevo_admin
        return self.administrador

    def agregar_estacionamientos(self, cantidad_extra):
        self.num_estacionamientos += cantidad_extra
        return self.num_estacionamientos