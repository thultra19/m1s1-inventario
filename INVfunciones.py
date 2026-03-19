def registrar_productos (nombre_producto, cantidad_producto, precios_producto):

    total_producto = cantidad_producto * precios_producto
    print(f"Producto: {nombre_producto} | Precio: {precios_producto} | Cantidad: {cantidad_producto} | Total: {total_producto}")
    print ("el producto a sido registrado")
    return total_producto


def calcular_valor_inventario(inventario):

    valor_total = 0
    cantidad_total = 0

    for producto in inventario:
        cantidad_total += producto["Cantidad"]
        valor_total += producto["Total"]

    return valor_total, cantidad_total
