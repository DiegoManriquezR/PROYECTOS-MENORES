### PRACTICAS AGREGAR UNA SOLA LISTA DE DATOS
id=[1,2,3,4,5]
nombre=['ANA','LUIS','PEPE','ADAN','EVA']
edad=[21,31,25,27,33]
personas=[]
ac=0

for i in range(5):
    print(id[i],nombre[i],edad[i])
    personas.append(id[i])
    personas.append(nombre[i])
    personas.append(edad[i])
    # buscar el mayor
    viejo=max(edad)
    if edad[i]==viejo:
        nom=nombre[i]
    # promedio de las edades
    ac+=edad[i]
promedio=ac/len(edad)
print('EL MAS VIEJO',nom,'PROMEDIO EDADES ',promedio)
print(personas)

for j in range(len(personas)):
    print(personas[j],end=' ')
