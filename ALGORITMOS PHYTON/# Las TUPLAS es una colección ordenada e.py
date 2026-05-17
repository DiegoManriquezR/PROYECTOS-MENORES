# Las TUPLAS es una colección ordenada e INMUTABLE de elementos.
# Las tuplas están ordenadas, significa que los elementos tienen un orden y no cambiará.
# Los elementos de tupla están ordenados, son inmutables y permiten valores duplicados.
# Los elementos de tupla están indexados,  índice [0], el segundo elemento tiene índice [1], etc.
tupla = (1, 2, 5, 7, 9)
print(tupla)  

# Los elementos de la tupla pueden ser de cualquier tipo de datos:
tupla1 = ("abc", 34, True, 40.0)

# A pesar de que las tuplas puedan parecerse a las listas, 
# frecuentemente se utilizan en distintas situaciones y para distintos propósitos. 
# Las tuplas se usan normalmente para una secuencia heterogénea de elementos 
# que son accedidos al desempaquetar o  indexar 

# CONVERTIR LISTA EN TUPLA
MiLista = ["Curico", "Talca", "Concepcion","Rancagua","Valparaiso","Santiago","Licanten"]
Ciudades=tuple(MiLista)    # Constructor de Tuplas 
print(Ciudades)
for i in Ciudades:
    print(i)

### Crea una tupla con números e indica el numero con mayor valor y el que menor tenga. 
numeros = (5,4,3,-2,1,6,455,3,66,666,6,6)
maximo = numeros[0]   # asume el valor inicial como maximo 
minimo = numeros[0]
 
for i in numeros:
    if i > maximo:
        maximo = i
 
    if i < minimo:
        minimo = i
 
print("El maximo es ",maximo)
print("El minimo es ",minimo)

if 66 in numeros:
    print(numeros.index(66))
else:
    print("el numero no esta")
 


