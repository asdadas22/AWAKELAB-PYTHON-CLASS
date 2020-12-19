import paquete_cientifico as pc



if __name__ == "__main__":
    financiera_01_ref = pc.crear_financiera("Karol-Dance. consultores")
    print(financiera_01_ref)

    print(pc.lista_todos_los_clientes[0].girar(500000)[0])
    print(pc.lista_todos_los_clientes[0].girar(50000)[0])
    print(pc.lista_todos_los_clientes[0].abonar(50000))

    print(pc.lista_todos_los_clientes[1].girar(40000)[0])
    print(pc.lista_todos_los_clientes[1].girar(30000)[0])
    print(pc.lista_todos_los_clientes[1].abonar(10000))

    print(pc.lista_todos_los_clientes[2].girar(100000)[0])
    print(pc.lista_todos_los_clientes[2].girar(30000)[0])
    print(pc.lista_todos_los_clientes[2].abonar(10000))


    cliente_envio_id = financiera_01_ref.lista_clientes[0].cliente_id
    cliente_destino_id = financiera_01_ref.lista_clientes[2].cliente_id

    print(financiera_01_ref.transferir(cliente_envio_id, cliente_destino_id, 50000))

    print("==============")

    print(financiera_01_ref.lista_clientes[0].saldo)
    print(financiera_01_ref.lista_clientes[2].saldo)

    print (" ================= ")

    cliente_envio_id_financiera = financiera_01_ref.lista_clientes[1].cliente_id

    print(financiera_01_ref.transferir(cliente_envio_id_financiera, "", 500, False))

    print(financiera_01_ref.lista_clientes[1].saldo)

    print(pc.lista_todos_los_clientes[3].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[4].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[5].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[6].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[7].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[8].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[9].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[10].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[11].girar(1000000)[0])
    print(pc.lista_todos_los_clientes[12].girar(1000000)[0])

    # Si se quiere verificar el funcionamiento de agregar clientes. jugar con las lineas 
    # de la 52 a la 50
    print(financiera_01_ref.agregar_cliente("Pepito"))

    print(financiera_01_ref)

    for i in financiera_01_ref.lista_clientes:
        print(i)
    
    print(financiera_01_ref.get_giros_abonos_info())

    