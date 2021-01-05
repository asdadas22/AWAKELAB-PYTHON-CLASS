import paquete_cientifico as pc


if __name__ == "__main__":
    condominio_01 = pc.CondominioVertical("Pedro montt", [], [], 10, [], "cuenta corriente", 5, 1, 100, 50,
    "pepito", 120, 500, "vivienda", "jardines del bosque", 20, 322344525)
    print(condominio_01.condominio_vertical_info())
    print(condominio_01.get_administrador())
    condominio_01.set_administrador("Alberto")
    print(condominio_01.get_administrador())