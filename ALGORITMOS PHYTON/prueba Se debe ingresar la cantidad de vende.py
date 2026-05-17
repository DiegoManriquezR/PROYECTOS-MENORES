## Se debe ingresar la cantidad de vendedores, el nombre del vendedor, el monto de las ventas realizado.
## Calcular las ganancias del vendedor, considerando que él gana el 15% del monto de las ventas, si esta es mayor a $ 300.000, si no es así sólo gana el 10%. 
## Mostrar además el nombre del vendedor que vendió más.

cantvend = int(input("Ingrese la cantidad de vendedores: "))
nomvendedormax = ""
ventasmax = 0

for i in range(cantvend):
    nomvend =int(input('Ingrese el nombre del vendedor'))
    monvent = float(input('Ingrese el monto de ventas para'))
    if monvent > 300000:
        gan = monvent * 0.15
    else:
        gan = monvent * 0.10
    print('Ganancias de', monvent,'$',gan)
    if monvent > ventasmax:
        ventasmax = monvent
        nomvendedormax = monvent
print('el venderot que vendio mas fue',nomvendedormax, 'que vendio',ventasmax)