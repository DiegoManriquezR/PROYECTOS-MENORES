## 3 LISTAS MOSTRAR LA PERSONA MAYOR Y EL PROMEDIO DE LAS EDADES
correlativos=[1,2,3,4,5]
nombre=['ana','luis','juan','sofia','raul']
edad=[22,20,24,23,19]
personas=[]
ac=0
for i in range(5):
    print(correlativos[i],nombre[i],edad[i])
    personas.append(correlativos[i])
    personas.append(nombre[i])
    personas.append(edad[i])
    oldman=max(edad)
    if edad[i]==oldman:
        nom=nombre[i]
    ac+=edad[i]   ##suma de edades
promedio=ac/len(edad)
print('el mayor es',nom,'el promedio de las edades es',promedio)

for j in personas:
    print(f'\t{j}',end='')


### asignaturas
import random
hardware=[]
bbdd=[]
algebra=[]
ciudadania=[]

for i in range(4):
    hardware.append(random.randint(1,7))
    bbdd.append(random.randint(1,7))
    algebra.append(random.randint(1,7)) 
    ciudadania.append(random.randint(1,7))

promedio=[]
for j in range(4):
    promedio.append((hardware[j]+bbdd[j]+algebra[j]+ciudadania[j])/4)

for k in range(4):
    print(hardware[k],bbdd[k],algebra[k],ciudadania[k], ' = ' ,promedio[k])

