
## INGRESAR N VENTAS Y CADA VENTA CON N PRODUCTOS
## INGRESAR POR CADA PRODUCTO NOMBRE Y KILOS VENDIDOS
## MOSTRAR KILOS POR CADA PRODUCTO Y EL PRODUCTO MAS VENDIDO
## SUMA TOTAL DE KILOS VENDIDOS DE TODAS LAS VENTAS


cant=int(input('CANTIDAD DE VENTAS '))
mayor=sumaK=cantpro=0
for i in range(cant): #CICLO DE VENTAS
    prod=int(input('CANTIDAD DE PRODUCTOS'))
    cantpro+=prod
    for j in range(prod):
        nombre=input('nombre producto')
        kg=int(input('kilos'))
        sumaK+=kg
        if kg>mayor:
            mayor=kg
            nom=nombre
    print('nombre',nombre,'kilos vendidos',kg)
print('mas vendido',nom)
print('cantidad productos vendidos ',cantpro,'suma kilos vendidos',sumaK)