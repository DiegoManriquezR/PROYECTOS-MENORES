## Se debe ingresar el monto de la venta y la categoría del producto. 
## Las categorías son: "Vestuario", "Ropa deportiva", "Calzado", "accesorios" 
## Se debe obtener el monto total de las ventas en todas las categorías.  
## Mostrar el monto de las ventas de “Ropa deportiva”.
## Mostrar la cantidad de categoría “Calzado”, vendida.  

n=int(print('INGRESE MONTO DE LA VENTA'))
cat=int(print(' INGRESE CATEGORIA DEL PRODUCTO 1.VESTUARIO 2.ROPA DEPORTIVA 3.CALZADO 4.ACCESORIOS'))
montoropadepotiva=0
cantidadcalzado=0
sum=float()

for i in range(n)  :
    cat = n
    monto = n
    sum+=n

    if cat == 2:
        montoropadepotiva += monto
    elif cat == 3:
        cantidadcalzado += monto
print('EL TOTAL DEL MONTO VENDIDO DE ROPA DEPORTIVA ES ',montoropadepotiva)
print('LA CANTIDAD TOTAL DE CALZADO VENDIDO ES', cantidadcalzado)