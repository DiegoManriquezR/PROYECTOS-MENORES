#generar 10 numeros aleatorios guardarlos en una lista
#en otra lista elevarlos a la potencia y guardarlos
#mostrar la lista de numeros orenada y la lista potencias al reves

import random
#crear 2 listas
numeros=[]
potencias=[]
#ciclo ingresar numeros aleatorios en la lista
for i in range(10):
    numeros.append(random.randint(1,100))

for j in range(10):
    potencias.append(numeros[j]**2)

numeros.sort()
potencias.sort()
potencias.reverse()
print(numeros)
print(potencias)

print('############################################################################################################################################################################')
#buscar numeros repetidos en una tupla
numeros_tupla=(5,6,7,6,66,666,66,7,3,6,666,8)
nro=int(input('ingrese numero a buscar '))
contar=0
for i in numeros_tupla:
    if nro== i:
        contar+=1
print('hay ',contar,'numeros repetidos')

### ordenamiento listas
## los numeros de una lista guardalos en otra de mayor a menor

lista1=[1,11,2,22,3,33,4,44,5,55,6,66,7,77,8,88,9,99]
lista2=[]

print(lista1.index(max(lista1)))

for i in range(len(lista1)):
    lista2.append(lista1[lista1.index(max(lista1))])
    lista1.pop(lista1.index(max(lista1)))


print(lista2)