cadena='lionel andrés messi cuccittini   '
print(cadena.upper()) # mayusculas
print(cadena.lower()) # minusculas
print(cadena.strip()) # elimina espacios principio y al final
print(cadena.capitalize()) #mayuscula la primera

nombre=cadena.lower()

for i in nombre:
    print(i,end=' ')

nom=list(nombre)
for j in range(len(nom)):
    print(j,end=' ')
    if nom[j]=='a' or nom[j]=='i' or nom[j]=='u':
        nom[j]='&'
print(nom)

messi=','.join(nom)
print(messi)

## cifrado 2.0
abc='abcdefghijklmnopqrstuvwxyz'
n=input('ingrese su nombre')
nombre=list(n)

for i in range(len(nombre)):
    if nombre[i] in abc:
        nombre[i]=abc[i]

print(nombre)


### correo
correo='rosaurodelasmercedesAinacapmail.cl'

cor=list(correo)
for j in range(len(cor)):
    if cor[j]=='A':
        cor[j]='@'
print(cor)