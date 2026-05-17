###controlar flujo es mejor while###



# Crear listas para nombres, precios y cantidades vendidas
nombres = []
precios = []
cantidades_vendidas = []

while True:
    print("\nMenú:")
    print("1. Introducir un artículo nuevo")
    print("2. Hacer una venta")
    print("3. Mostrar información")
    print("4. Borrar un artículo")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        nombre = input("Ingresa el nombre del artículo: ")
        precio = float(input("Ingresa el precio del artículo: "))
        nombres.append(nombre)
        precios.append(precio)
        cantidades_vendidas.append(0)  # Inicializamos con 0

    elif opcion == 2:
        nombre_venta = input("Ingresa el nombre del producto a vender: ")
        if nombre_venta in nombres:
            indice = nombres.index(nombre_venta)
            cantidad_vendida = int(input("Ingresa la cantidad vendida: "))
            cantidades_vendidas[indice] += cantidad_vendida
        else:
            print("El producto no existe.")

    elif opcion == 3:
        print("\nInformación de productos:")
        print("Nombre\tPrecio\tCantidad Vendida")
        for i in range(len(nombres)):
            print(f"{nombres[i]}\t{precios[i]}\t{cantidades_vendidas[i]}")

        # Calcular artículo más vendido y menos vendido
        max_vendido = nombres[cantidades_vendidas.index(max(cantidades_vendidas))]
        min_vendido = nombres[cantidades_vendidas.index(min(cantidades_vendidas))]
        print(f"\nArtículo más vendido: {max_vendido}")
        print(f"Artículo menos vendido: {min_vendido}")

    elif opcion == 4:
        nombre_borrar = input("Ingresa el nombre del artículo a borrar: ")
        if nombre_borrar in nombres:
            indice_borrar = nombres.index(nombre_borrar)
            del nombres[indice_borrar]
            del precios[indice_borrar]
            del cantidades_vendidas[indice_borrar]
            print("Artículo borrado.")
        else:
            print("El artículo no existe.")

    elif opcion == 5:
        break