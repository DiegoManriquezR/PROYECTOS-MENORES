def login(nombre,password):
    if nombre=='admin' and password=='qwerty':
        return True
    else:
        return False

x=1
intento=0
while x!= 0:
    usuario=input('nombre Usuario: ')
    clave=input('Password: ')
    entrar=login(usuario,clave)
    intento+=1
    if entrar==False:
        print('Error, nombre de usuario o contraseña incorrecta')
    if entrar==True or intento==3:
        break
if entrar==True:
    print('Bienvenido al sistema ....')
else:
    print('No haz entrado al sistema o haz superado el numero de intentos')



