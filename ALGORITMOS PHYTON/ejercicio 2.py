#II. Construya un script que calcule lo siguiente:

##1.	Cree tupla que contenga 10 números.
##2.	Una lista que permita ingresar 10 números, menores a 10.
##3.	Multiplicar ambos arreglos en un tercer vector. 

##	Mostrar los tres vectores. 

tupla1=(1,2,3,4,5,6,7,8,9,10)
lista1=[]
resultado=[]
for i in range(10):
    num=float(input(f'Digite numero {i+1} menor a 10 : '))
    if num < 10:
        lista1.append(num)
    else:
        print("El número debe ser menor a 10. Inténtalo nuevamente.")

resultado=[a * b for a, b in zip(tupla1,lista1)]
print("Tupla de números:", tupla1)
print("Lista de números ingresados:", lista1)
print("resultado de la multiplicación:", resultado)


### DIEGO MANRIQUEZ
### JHONNY SUAZO