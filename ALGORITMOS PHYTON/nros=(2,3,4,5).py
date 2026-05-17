nros=(2,3,4,5) ###tuplas
nros2=(6,7,8,9,) ###tuplas
suma=[] ###lista
for i in range(len(nros)):
    suma.append(nros[i]+nros2[i])

print(suma)

print('######################################################################')
asignaturas=('MATEMATICAS','INGLES','FISICA','HISTORIA','ARTES')
alumnos=['PEPE','MANUEL','JULIO']
notas=[]

for i in range(len(alumnos)):
    print('alumno',alumnos[i])
    sum=0
    for j in range(len(asignaturas)):
        print('RAMO: ',asignaturas[j])
        nota=float(input('INGRESE LA NOTA '))
        sum+=nota
        notas.append(nota)
    prom=sum/len(asignaturas)
    print(alumnos[i],'PROMEDIO',prom)

for i in range(len(alumnos)):
    print('ALUMNO',alumnos[i])
    for j in range(len(asignaturas)):
        print(asignaturas[j],' = ',notas[j])