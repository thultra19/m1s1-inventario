nombre_producto = str(input("Ingrese el nombre del producto: "))

verifica_cantidad = True
verifica_precio = True

while verifica_cantidad:

    cantidad_producto = (input("Ingrese la cantidad del producto: "))

    if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
        cantidad_producto = int(cantidad_producto)
        verifica_cantidad = False
    else:
        print(f"ven aca, cuando has visto tu que una cantidad de algo sea '{cantidad_producto}', colocame un numero entero valido")
    

while verifica_precio:

    precios_producto = (input("Ingrese el precio del producto: "))

    if precios_producto.isdigit() and float(precios_producto) > 0:
        precios_producto = float(precios_producto)  
        verifica_precio = False  
    else:
        print(f"ven aca, cuando has visto tu que un precio sea '{precios_producto}', colocame un numero valido")
    

total_producto = cantidad_producto * precios_producto
print(f"Producto: {nombre_producto} | Precio: {precios_producto} | Cantidad: {cantidad_producto} | Total: {total_producto}")