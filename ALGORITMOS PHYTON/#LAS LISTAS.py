#LAS LISTAS 
numeros =[7,11,13,17,23,27,31,37,39,41,46]
#Acceder a los elementos de una lista
print(numeros)
print(numeros[3])
print("Largo de la lista: ",len(numeros))
#Python (Arrays) permiten Indexación negativa
#La indexación negativa significa empezar desde el final -1 
# se refiere al último elemento, -2 se refiere al penúltimo

print("al derecho ",numeros[4:11])
print(numeros[-11:-4])
print(numeros[-11:-1])
# Al reves.
print(list(reversed(numeros)))

print("#######  CICLOS ########")

for i in range(len(numeros)):
    print(numeros[i])

i = 0
while i < len(numeros):
  print(numeros[i])
  i = i + 1 

###### OPERACIONES CON LISTAS

print("los 10 primeros numeros") 
lista=[]

i=1
while i<=10:
    lista.append(i)  #agrega elemento al final
    i=i+1
print(lista)


# insertar un numero al final 
num=[]
for i in range(4):
    nro = int(input("Ingrese un numero: "))
    num.append(nro)

num.sort()   #Ordena la lista
print(num,end=" ")
num.sort(reverse=True)  #muestra al reves
print(num, end=" ")


"""   METODOS DE LISTAS 
append() Añade un elemento al final de la lista
clear() Elimina todos los elementos de la lista
copy() Devuelve una copia de la lista
count() Devuelve el número de elementos con el valor especificado
extend() Añade los elementos de una lista (o cualquier iterable), al final de la lista actual
index() Devuelve el índice del primer elemento con el valor especificado
insert() Añade un elemento en la posición especificada
pop() Elimina el elemento en la posición especificada
remove() Elimina el elemento con el valor especificado
reverse() Invierte el orden de la lista
sort() Ordena la lista
"""
## end=' ' ,mostrar hacia el lado


