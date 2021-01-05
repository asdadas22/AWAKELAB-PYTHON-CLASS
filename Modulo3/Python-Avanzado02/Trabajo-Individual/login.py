class Usuario:

    intentos_de_login = 0

    def __init__(self, nombre, apellido, mail, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono

    def describir_usuario(self):
        return "El nombre del usuario es: %s %s, el mail del usuario es: %s" \
                " El telefono del usuario es: %s" \
                % (self.nombre, self.apellido, self.mail, self.telefono)

    def saludar_usuario(self):
        return "Hola %s %s muchas gracias por logear en asd.com" \
                % (self.nombre, self.apellido)

    def incrementar_inicios_de_sesion(self):
        self.intentos_de_login += 1
        return self.intentos_de_login

    def reset_intentos_login(self):
        self.intentos_de_login = 0
        return self.intentos_de_login


## TESTEO DE LOGIN ##

usuario_01 = Usuario("Ruben", "Suarez", "asda@gmail.com", "133")

print(usuario_01.describir_usuario())
print(usuario_01.saludar_usuario())


for i in range(0, 4):
    print(usuario_01.incrementar_inicios_de_sesion())


print(usuario_01.reset_intentos_login())