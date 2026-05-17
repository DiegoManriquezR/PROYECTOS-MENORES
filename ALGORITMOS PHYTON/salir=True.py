salir=True
ac=0
while salir==True:
    nro=int(input('ingrese un numero, para salir presione 0. '))
    ac+=nro
    print(nro,'\t')
    if nro==0:
        #break
       salir=False
print('sumatoria de los numeros ingresados ',ac)
