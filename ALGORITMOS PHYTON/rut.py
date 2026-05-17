def datos_personales(rut,*persona):
    print(f'\n Datos Personales: Rut:{rut} ')
    for persona in persona:
        print(f'\n {persona}')

rut=input('ingrese rut')
nombre=input('ingrese nombre')
edad=int(input('ingrese su edad'))
comuna=input('ingrese su comuna')
datos_personales(rut,nombre,edad,comuna)
datos_personales(rut,nombre)
datos_personales(rut,edad,comuna)
datos_personales(rut,'',edad,'CURICÓ')