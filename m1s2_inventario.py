import INVfunciones 
sw=True
print('Bienvenido a al sistema de manejo de inventario de Riwi\n')
inventario=[]

while sw:
    
    print('Que le gustaria hacer?\n')
    print('1.Agregar producto')
    print('2.Mostrar inventario')
    print('3.Calcular estadísticas')
    print('4.Salir')
    proceso = input().strip().lower()

    match proceso:

        case "1" | "agregar":

            nombre_producto = str(input("Ingrese el nombre del producto: "))
            cantidad_producto = (input("Ingrese la cantidad del producto: "))
            precios_producto = (input("Ingrese el precio del producto: "))

            verifica_cantidad = True
            verifica_precio = True

            while verifica_cantidad:

                if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
                    cantidad_producto = int(cantidad_producto)
                    verifica_cantidad = False
                else:
                    print(f"ven aca, cuando has visto tu que una cantidad de algo sea '{cantidad_producto}', colocame un numero entero valido")
    
            while verifica_precio:

                if precios_producto.isdigit() and float(precios_producto) > 0:
                    precios_producto = float(precios_producto)  
                    verifica_precio = False  
                else:
                    print(f"ven aca, cuando has visto tu que un precio sea '{precios_producto}', colocame un numero valido")
            
            retorno_agregar = INVfunciones.registrar_productos(nombre_producto, cantidad_producto, precios_producto)
            print(retorno_agregar)
            agregador = {"Nombre":nombre_producto, "Cantidad":cantidad_producto, "Precio unitario":precios_producto, "Total":retorno_agregar}
            inventario.append(agregador)

        
        case "2" | "mostrar" | "inventario":
            
            if len(inventario) == 0:
                print('el inventario esta vacio')
            else:
                for i, c in enumerate (inventario,start = 1):
                    print(f'{i}. {c}')

        case "3" | "calcular" | "estadisticas":

            if len(inventario) == 0:
                print('el inventario esta vacio')
            else:
                valortotalinventario, cantidadtotal = INVfunciones.calcular_valor_inventario(inventario)
                print(f'El valor total del inventario es: {valortotalinventario}')
                print(f'La cantidad total de productos es: {cantidadtotal}')
        
        case "4" | "salir":
            print('gracias por usar el programa')
            
            sw = False
        
        case _:
            print('opcion no valida, porfavor selecione una opcion valida de la lista o escriba "salir" para cerrar el programa.')
