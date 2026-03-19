def registrar_productos (nombre_producto, cantidad_producto, precios_producto):

    total_producto = cantidad_producto * precios_producto
    print(f"Producto: {nombre_producto} | Precio: {precios_producto} | Cantidad: {cantidad_producto} | Total: {total_producto}")
    print ("el producto a sido registrado")
    return total_producto
