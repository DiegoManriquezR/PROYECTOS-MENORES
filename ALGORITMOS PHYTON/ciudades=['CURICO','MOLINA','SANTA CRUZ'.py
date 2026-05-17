ciudades=['CURICO','MOLINA','SANTA CRUZ','TENO','SAGRADA FAMILIA','LICANTEN']

ciudades.append('VICHUQUEN')
print(ciudades)
ciudades.insert(2,'RAUCO')
print(ciudades)
ciudades[4]='SAN FERNANDO'
print(ciudades)
ciudades.sort()
print(ciudades)
print('MAYOR ',max(ciudades))
print('MENOR ',min(ciudades))

for i in ciudades:
    print(i)

for i in range(len(ciudades)):
    print(i,ciudades[i])


