import uuid
import random


lista_nombres = ["Ruben", "Natalia", "Elizabeth", "Juan", "Pamela", "Coni", "Luis", "Luisa", "Francisco"]

lista_todos_los_clientes = []

class Clientes:
    
    saldo = 0
    financiera_ref = None
    
    def __init__(self, nombre, cliente_id):
        self.nombre = nombre
        self.cliente_id = cliente_id

    def girar(self, nuevo_saldo):
        if  self.saldo - nuevo_saldo >= -1000000:
            self.saldo -= nuevo_saldo
            self.financiera_ref.giros_totales()
            self.financiera_ref.descontar_saldo_institucional(nuevo_saldo)
            return ["La operacion fue existosa su nueva deuda es: %s" % (self.saldo), True]
        return ["No se puede realizar la operacion porque su saldo supera el limite \n" \
                "Su saldo disponible es %s" % (self.saldo + 1000000), False]

    def abonar(self, nuevo_saldo):
        self.saldo += nuevo_saldo
        self.financiera_ref.abonos_totales()
        return "La operacion de abonar fue existosa su nuevo saldo es: %s" % (self.saldo)

    def mostrar_saldo(self):
        return "El saldo del cliente es %s" % (self.saldo)

    def set_financiera_ref(self, financiera):
        self.financiera_ref = financiera
        return True

    def __str__(self):
        return "Nombre: %s --- cliente_id: %s --- saldo: %s" % (self.nombre, self.cliente_id, self.saldo) 


class Financieras:

    max_saldo_institucional = 100000000
    current_linea_credito = 0

    def __init__(self, nombre, lista_clientes, financiera_id, saldo_institucional = 100000000):
        self.nombre = nombre
        self.financiera_id = financiera_id
        self.saldo_institucional = saldo_institucional
        self.lista_clientes = lista_clientes

        self.giros_totales_count = 0
        self.abonos_totales_count = 0

    def __str__(self):
        return "nombre: %s -- financiera_id: %s --- saldo institucional: %s \n" \
                "linea de credito total: %s --- giros: %s --- abonos: %s \n" \
                 % (self.nombre, self.financiera_id, self.saldo_institucional, self.current_linea_credito, 
                    self.abonos_totales_count, self.giros_totales_count)

    # funcion para agregar cliente solo si linea de credito no es mayor al 10% de saldo institucional
    def agregar_cliente(self, nombre_cliente):
        if self.check_max_linea_credito():
            cliente = Clientes(nombre_cliente, uuid.uuid4().hex)
            self.lista_clientes.append(cliente)
            return "Cliente creado agregado correctamente"
        else:
            return "No se puede agregar un nuevo cliente porque \n la linea de credito supero el 10'%' institucional"

    # elimina un cliente by id
    def eliminar_cliente(self, cliente_id):
        for cliente in self.lista_clientes:
            if cliente.cliente_id == cliente_id:
                self.lista_clientes.remove(cliente)
                return "Cliente borrado correctamente"
            else:
                return "Cliente no se encuentra en la base de datos."        

    def transferir(self, id_envio, id_destino, monto, entre_clientes=True):
        cliente_envio = ""
        cliente_destino = ""
        if entre_clientes:

            for cliente_que_envia in self.lista_clientes:
                if cliente_que_envia.cliente_id == id_envio:
                    cliente_envio = cliente_que_envia
                    break
            
            for cliente_que_recibe in self.lista_clientes:
                if cliente_que_recibe.cliente_id == id_destino:
                    cliente_destino = cliente_que_recibe
                    break
            
            if cliente_envio != "" and cliente_destino != "":
                if cliente_envio.girar(monto)[1]: 
                    cliente_destino.abonar(monto)
                    return "La transferencia se realizo con exito"
                else:
                    return "La operacion no fue realizada porque supera el limite de su saldo"

        else:

            for cliente_que_envia in self.lista_clientes:
                if cliente_que_envia.cliente_id == id_envio:
                    cliente_envio = cliente_que_envia
                    break
            if cliente_envio != "":
                if cliente_envio.girar(monto)[1]:
                    self.agregar_saldo_institucional(monto)
                    return "La trnasferencia entre cliente y financiera fue exitosa"
                else:
                    return "La operacion no fue realizada porque supera el limite de su saldo"


    def giros_totales(self):
        self.giros_totales_count += 1
        return self.giros_totales_count

    def abonos_totales(self):
        self.abonos_totales_count += 1
        return self.abonos_totales_count

    def mostrar_saldo_institucional(self):
        return self.saldo_institucional

    def check_max_linea_credito(self):
        if self.saldo_institucional >= 90000000:
            return True
        return False
            
    def get_giros_abonos_info(self):
        return "Los giros totales son: %s --- Los abonos totales son: %s" % (self.giros_totales_count, self.abonos_totales_count)

    def descontar_saldo_institucional(self, monto):
        self.saldo_institucional -= monto

    def agregar_saldo_institucional(self, monto):
        self.saldo_institucional += monto

def obtener_nombre_random(lista_nombres):
    tmp_rnd = random.randint(0, len(lista_nombres) - 1)
    return lista_nombres[tmp_rnd]

def crear_cliente(nombre):
    cliente = Clientes(nombre, uuid.uuid4().hex)
    lista_todos_los_clientes.append(cliente)
    return cliente


def crear_financiera(nombre_financiera):
    lista_clientes = []
    for i in range(0, 13):
        tmp_nombre = obtener_nombre_random(lista_nombres)
        cliente = crear_cliente(tmp_nombre)
        lista_clientes.append(cliente)

    financiera = Financieras(nombre_financiera, lista_clientes, uuid.uuid4().hex)
    
    for cliente in financiera.lista_clientes:
        cliente.set_financiera_ref(financiera)

    return financiera


