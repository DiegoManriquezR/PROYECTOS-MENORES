"""
Una empresa necesita procesar una lista con los totales de ventas de los últimos 6 meses, 
para ello, solicite al usuario el ingreso de estos montos (en pesos chilenos) para agregarlos
a una lista que será enviada a una función que realizara su proceso. 
La función debe eliminar todas las ventas negativas (registros ingresados erróneamente con montos inferiores a 0),
ordene las ventas de manera ascendente y finalment  e devuelva la lista procesada. 
Asegúrese de validar que todos los elementos ingresados en la lista sean números enteros.
"""
# importamos las funciones propias a utilizar desde miModulo
from miModulo.validaciones import esEntero, esNegativo

def procesarVentas(ventas):
    # Validamos que todos los elementos de la lista sean positivos  
    for venta in ventas:
        if esNegativo(venta):
            # recuperamos el indice del elemento
            indice = ventas.index(venta) 
            # eliminamos el elemento de la lista
            ventas.pop(indice)

    # Ordenamos la lista en orden ascendente
    ventas.sort()
    # Retornamos la lista
    return ventas

ventas=[] # Declaramos una lista para el ingreso de elementos
for mes in range(1,7):
    while True:
        venta = input(f"ingrese el monto total de ventas del mes {mes}: ")
        if esEntero(venta): # verificamos si es un entero
            break
    ventas.append(venta) # agreegamos el elemento a la lista
    
# mostramos el resultado    
print(procesarVentas(ventas))

