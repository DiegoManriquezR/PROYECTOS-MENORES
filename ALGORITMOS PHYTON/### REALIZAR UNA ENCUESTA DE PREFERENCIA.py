### REALIZAR UNA ENCUESTA DE PREFERENCIAS DE USUARIOS
## QUEREMOS SABER SI MENORES DE EDAD VEN SERIES Y ADULTOS MAYORES VEN TELENOVELAS
#EL PORCENTAJE DE MUJERES QUE VEN PELICULAS
# Y CANTIDAD DE VARONES QUE VEN DOCUMENTALES

n=int(input("cantidad encuestado"))
men=tls=0
sexo=0
chicas=0
peli=0
doc=0
for i in range (n):
    edad=int(input('ingrese su edad'))
    print('ingrese su sexo 1.mujer 2.hombre 3.otres')
    sex=int(input())
    print('seleccione una categoria 1.series 2.peliculas 3.telenovelas 4.documentales')
    categoria=int(input())
    if edad<18:   #menores que ven series
        if categoria==1:
            men+=1
    if edad>=65 and categoria==3:
        tls+=1 
    if sex==1:
        chicas+=1
        if categoria==2:
            peli+=1
            porcentaje=(peli/chicas)*100
    if sex==2 and categoria==4:
        doc+1
print('menores ',men)
print('mayores teleseries',tls)
print('mujeres peliculas ',porcentaje,'%')
print('hombres documentales',doc)
