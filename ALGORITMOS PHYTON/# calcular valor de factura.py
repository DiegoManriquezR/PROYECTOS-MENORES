# calcular valor de factura
def factura(neto,desc,impto):
    return neto-(neto*desc)+(neto*impto)



vta=int(input('ingrese monto venta $ '))
descuento=float(0.2)
iva=float(0.19)
total=factura(vta,descuento,iva)
print('$',total)

###