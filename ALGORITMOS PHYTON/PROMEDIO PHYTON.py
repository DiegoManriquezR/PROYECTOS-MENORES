
print('HOLA MUNDO')
#esto es un comentario
a=5
b=str(2)
c=int(7)
d=float(5.5)
print(a,b,c,d)

#print('ingrese una nota')
nota1=float(input('ingrese una nota'))
nota2=float(input('ingrese una nota'))
nota3=float(input('ingrese una nota'))
prom=(nota1+nota2+nota3)/3
print('promedio ',prom)
if prom>=4:
    print('Aprobado')
else:
    print('Reprobado')


##tabla de multiplicar
    tb=int(input('ingrese numero de la tabla'))
for i in range(12):
    print(tb,' x ',i,' = ',tb*i)