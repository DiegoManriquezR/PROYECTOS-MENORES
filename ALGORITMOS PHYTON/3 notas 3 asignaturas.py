    ### ingresar 3 notas en 3 asignaturas y obtener el promedio
algebra=[]
bbdd=[]
hys=[]
promedio=[]

for i in range (3):
    nota=float(input('ingrese una nota'))
    algebra.append(nota)
    nota1=float(input('ingrese una nota'))
    bbdd.append()
    nota2=float(input('ingrese una nota'))
    hys.append(nota2)

for j in range(3):
    promedio.append((algebra[j]+bbdd[j]+hys[j])/3)

for k in range(3):
    print(algebra[k],bbdd[k],hys[k],' = ',promedio[k])