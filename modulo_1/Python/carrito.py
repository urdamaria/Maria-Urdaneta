def mostrar_productos(productos):
    print("\nProductos Disponibles") 
    for codigo, detalles in productos.items():
        print(f"[{codigo}] {detalles['nombre']} - ${detalles['precio']:.2f}")

def agregar_al_carrito(carrito, productos):
    while True:
        codigo_producto = input("Ingrese el código del producto a agregar: ").lower()
        if codigo_producto == 'listo':
            break
        if codigo_producto in productos:
            try:
                cantidad = int(input(f"Ingrese la cantidad de '{productos[codigo_producto]['nombre']}' que desea: "))
                if cantidad > 0:
                    if codigo_producto in carrito:
                        carrito[codigo_producto]['cantidad'] += cantidad
                    else:
                        carrito[codigo_producto] = {
                            'nombre': productos[codigo_producto]['nombre'],
                            'precio': productos[codigo_producto]['precio'],
                            'cantidad': cantidad
                        }
                    print(f"{cantidad} x '{productos[codigo_producto]['nombre']}' agregado(s) al carrito.")
                else:
                    print("La cantidad debe ser un número positivo.")
            except ValueError:
                print("Cantidad inválida. Por favor, ingrese un número.")
        else:
            print("Código de producto no válido. Intente de nuevo.")

def ver_carrito(carrito):
    print("\nTu Carrito de Compras")
    if not carrito:
        print("El carrito está vacío.")
        return 0 # Retorna 0 si el carrito está vacío para el subtotal

    subtotal = 0
    for codigo, item in carrito.items():
        total_item = item['cantidad'] * item['precio']
        subtotal += total_item
        print(f"{item['cantidad']} x {item['nombre']} (${item['precio']:.2f} c/u) = ${total_item:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    return subtotal

def calcular_total(subtotal, tasa_impuesto):
    impuestos = subtotal * tasa_impuesto
    total_final = subtotal + impuestos
    print(f"Impuestos ({tasa_impuesto*100:.0f}%): ${impuestos:.2f}")
    print(f"Total a pagar: ${total_final:.2f}")

def main():
    #Función principal del programa del carrito de compras.
    productos = {
        '1': {'nombre': 'Laptop HP', 'precio': 850.00},
        '2': {'nombre': 'Teclado Mecánico', 'precio': 75.50},
        '3': {'nombre': 'Mouse Inalámbrico', 'precio': 25.00},
        '4': {'nombre': 'Monitor 24"', 'precio': 150.99},
        '5': {'nombre': 'Webcam HD', 'precio': 49.99}
    }
    carrito = {}
    tasa_impuesto = 0.16 # Tasa de impuesto del 16%

    print("¡Bienvenido al Carrito de Compras!")

    while True:
        print("\n Menú Principal")
        print("1. Mostrar productos")
        print("2. Agregar productos al carrito")
        print("3. Ver carrito")
        print("4. Calcular Total")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_productos(productos)
        elif opcion == '2':
            mostrar_productos(productos) # Mostrar productos antes de pedir que agregue
            agregar_al_carrito(carrito, productos)
        elif opcion == '3':
            ver_carrito(carrito)
        elif opcion == '4':
            subtotal = ver_carrito(carrito) # Muestra el carrito y obtiene el subtotal
            if carrito: # Solo calcula el total si hay algo en el carrito
                calcular_total(subtotal, tasa_impuesto)
            else:
                print("El carrito está vacío para calcular el total.")
        elif opcion == '5':
            print("Gracias… Vuelvan pronto, mil besitos, ¡Fué un placer!," \
            " Je je je je eh…Qué lindos...(entre dientes) Eh… ¿Ya se fueron?"\
            "¿Ya, ya por fin se fueron todos?¿No hay nadie? ¿Mm?¡Aaay!¡Qué aliviooo! ")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
