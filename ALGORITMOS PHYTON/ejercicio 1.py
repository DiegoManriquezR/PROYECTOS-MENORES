##I. Realizar un script que realice de un cifrado.   
##a.	Ingresar el nombre completo.
##b.	Asegurarse que la cadena esté en minúsculas. 
##c.	Convertir en vector. 
##d.	Durante el proceso reemplazar las vocales, en el caso de la a, e y o se reemplazarán por una @ y las vocales i y u con un $.

##•	Mostrar el nombre ingresado y el nombre cifrado.   


cadena=('diego esteban manriquez rodriguez')
nombre=cadena.lower()
for i in nombre:
    print(i,end=' ')

nom=list(nombre)
for j in range(len(nom)):
    print(j,end=' ')
    if nom[j]=='a' or nom[j]=='e' or nom[j]=='o':
        nom[j]='@'
    if nom[j]=='i' or nom[j]=='u':
        nom[j]='$'
print(nom)


### DIEGO MANRIQUEZ
### JHONNY SUAZO
