
def suma():
    n1=int(input('INGRESE UN NUMERO'))
    n2=int(input('INGRESE UN NUMERO'))
    sum=n1+n2
    print('LA SUMA ES ',sum)

def resta():
    n1=int(input('INGRESE UN NUMERO'))
    n2=int(input('INGRESE UN NUMERO'))
    rs=n1-n2
    return rs

def multiplicacion(a,b):
    r= a * b
    print('EL RESULTADO ES ',r)

def division(a,b):
    r= a / b
    return r









##CALCULADORA 4 OPERACIONES
opcion=0
print('INGRESE LA OPERACION 1.SUMA 2.RESTA 3.MULTIPLICACION 4.DIVISION')
opcion=int(input())

if opcion==1:   #realiza toda la operacion en la funcion
    suma()   

if opcion==2:   #realiza la operacion en la funcion y retorna resultado
    resultado=resta()
    print('LA RESTA ES ',resultado)

if opcion==3:   #se pasan los argumntos (valores) a la funcion y realiza el calculo
    n1=int(input('INGRESE UN NUMERO'))
    n2=int(input('INGRESE UN NUMERO'))
    multiplicacion(n1,n2)

if opcion==4:   #se pasan los argumentos y retornael resultado
   n1=int(input('INGRESE UN NUMERO'))
   n2=int(input('INGRESE UN NUMERO'))
   resultado=float(division(n1,n2))
   print(f'EL RESULTADO DE LA DIVISION ES {resultado:.2F}')