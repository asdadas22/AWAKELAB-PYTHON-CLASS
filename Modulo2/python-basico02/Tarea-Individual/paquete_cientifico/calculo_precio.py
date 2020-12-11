precio_libro = 24.95
precio_envio = 3
precio_envio_por_mayor = 0.75

def calculo_comprar_libros():
    cantidad_libros = int(input("Cuantos libros desea comprar: "))
    if cantidad_libros > 0:
        # Precio total de libros.
        total_precio_libros = cantidad_libros * precio_libro
        # Precio total de envio
        total_precio_envio = (precio_envio_por_mayor * (cantidad_libros - 1)) + precio_envio
        # Condicion para hacer descuento en caso de ser mas de 10 libros comprados
        if  cantidad_libros > 10:
            # aplico descuento directamente.
            total_libros_con_descuento = total_precio_libros * 0.6 + total_precio_envio
            # total_libros_con_descuento = total_precio_libros - (total_precio_libros * 0.4) + total_precio_envio
            return "El precio total con descuento es: {:.4f}".format(total_libros_con_descuento)
        else:
            return "El precio sin descuento es: " + str(total_precio_libros + total_precio_envio)