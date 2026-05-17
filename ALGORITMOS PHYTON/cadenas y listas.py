
lista1=[]
lista2=[]
lista3=[]

for i in range(3):
    lista1.append(int(input('ingrese numero')))
    numero=int(input('ingrese numero'))
    lista2.append(numero)
    lista3.append(lista1[i] + lista2[i])


for j in range(3):
    print(lista1[j],lista2[j],' = ',lista3[j])

### Convertircadenas y listas
nombre='ROSALIA ALBURQUENQUE MATAMALA'
print(nombre)
nom=list(nombre)
print(nom)

for i in nombre:
    print(i)
for j in range(len(nom)):
    print(nom[j],end='')
    if nom[j]=='A' or nom[j]=='E':
        nom[j]='@'

print(nom)