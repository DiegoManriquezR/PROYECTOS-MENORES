# CREACION y diccionario

nombres = {}   #Vacio
dict()      #Constructor 
nombres = dict([
      ('Nombre', 'Pedro'),
      ('Edad', 23),
      ('Rut', 10724882-1),
])
print(nombres)
print(type(nombres))

input()

# Los diccionarios se les pueden agregar elementos 
ciudades ={"nombre":"Curicó","hab":140000,"country":"Chile"}
ciudades["region"] = "Maule"
print(ciudades)

input()
# Borrar elementos 
del(ciudades["country"])

#Lectura secuencial del diccionario
for i in ciudades:
    print(i)
 
input()
#Esto muestra los indices (claves) y no los valores, para eso hay que indicar la clavec
for i in ciudades:
    print(ciudades[i])

#Para mostrar ambos
for i in ciudades:
    print(i,ciudades[i])

# Tambien con el metodo items() facilita la lectura en clave y valor de los elementos
for i, j in ciudades.items():
    print(i,j)

input()
#El método get() permite consultar por el valor de una clave 
#otro parámetro opcional, en el caso de que el valor no se encuentra.
w=ciudades.get("Maule")
x=ciudades.get("Talca","No esta")

print(x)
input()

# Crear Listas a partir de  diccionarios
vehiculos=[]
auto1 = {'Marca':'Chevrolet', 'Modelo':'Camaro', 'year':'1999'}
auto2 = {'Marca':'Ford', 'Modelo':'Mustang', 'year':'1990'}

vehiculos.append(auto1)
vehiculos.append(auto2)
print(vehiculos)
input()
# Los diccionarios permiten manejar las propiedades individuales de los registros 
# las listas nos permiten manejar todos en conjunto.  

for i in vehiculos:
    print(i ["Marca"], i ["Modelo"], i["year"])

capitales={'Chile':'santiago','España':'Madrid','Francia':'Paris','Argentina':'Buenos Aires' }
print(capitales)

print("Hay ", len(capitales), " paises") 
input()
for i,j in capitales.items():   #acceder al diccionario
    print("Pais ",i," Capital ",j)

capitales['Peru']='Lima'  #agregamos capital

if "Peru" in capitales:     # preguntamos si existe Peru
    print("Peru ",capitales['Peru'])
print("##############")
input()
# DICCIONARIOS MULTI VALOR 
paises ={'Pais':'Chile','Regiones':['Coquimbo','Valparaíso','Ohiggins','Maule','Ñuble','BioBio']}

print(paises)

for pais,region in paises.items():
    print(pais," ",region)

print(paises.items())      #lista de tuplas clave valor 
print(paises.keys())      # muestra las claves
print(paises.values())    # muestra valores 

paises['Regiones'].append("Metropolitana") #agregar valor a indice regiones
print(paises.items())

for c,v in paises.items():
    print("Clave ",c," valor ",v)

print(f"Pais: {paises['Pais']} "
      "con los siguientes Regiones:")
for i in paises['Regiones']:
    print("\t" + i)

aliens = []
alien = dict()
for alien_number in range(30):
    new_aliens = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aliens)
print(aliens)

print("-------------------")
registro = {'nombre':'Pablo',
          'trabajo':['desarrollo','community manager'],
          'web':'www.pablodev.org/pablo',
          'direccion':{'comuna':'Lontue','cod. postal':'3340000'}
          }
print(registro)
registro['nombre']
registro['trabajo']
print(registro['direccion']['comuna'])
for i,j in registro.items():
    print(i,j)










