## Construya un Algoritmo que permita leer los datos de N alumnos.
## Ingresar datos de alumnos: nombre, asignatura si la realiza por primera, segunda o tercera oportunidad y las 4 notas obtenidas en el semestre.
## Ingresar la cantidad de notas que tiene.
## Obtener promedio de notas de cada alumno con su nombre y mostrar si está aprobada o reprobada.
## Obtener el promedio de todos los alumnos.
## Obtener la cantidad de alumnos que tienen la asignatura por segunda o tercera vez.

cant=int(input('INGRESE CANTIDAD ALUMNOS'))
sum=float()
ac=float()
veces=0
vez=0
for i in range(cant):
    n=input('INGRESE NOMBRE ALUMNO')
    asig=(input('INGRESE NOMBRE ASIGNATURA'))
    input('INGRESE VECES QUE A CURSADO LA ASIGNATURA 1.PRIMERA VEZ 2.SEGUNDA VEZ 3.TERCERA VEZ')
    nnota=int(input('INGRESE CANTIDAD DE NOTAS'))
    for j in range(nnota):
     ac=float(0)
     nota=float(input('INGRESE UNA NOTA'))
     sum+=nota
     prom=sum/nnota
     ac+=prom
    print('DON(@)',n, 'SU PROMEDIO ES ',prom,'Y ESTA USTED')
    if prom>=4:
      print('APROBADO')
    else:
     print('REPROBADO')    
promtotal=ac/cant
print('EL PROMEDIO DE LOS ALUMNOS FUE ',promtotal)
if veces==2:
  veces+1
if vez==3:
  vez+1
print(veces,'alumnos repitieron el curso por segunda vez')
print(vez,'alumnos repitieron el curso por tercera vez')




     
