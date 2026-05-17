### calcular promedio de n estudiantes donde cada alumno ingresa notas hasta
## de notas que desee
### mostrar el promedio de cada alumno y el nombre del alumno con mejor nota

n=int(input('cantidad de estudiantes'))
mayor=0
for i in range(n):
    nombre=input('nombre de alumno '+str(i+1))
    sum=float()
    dato=1
    cont=0
    while dato != 0:
        nota=float(input('ingrese la nota'))
        sum+=nota
        cont+=1
        print('ingresar mas notas? 1.si 0.no')
        dato=int(input())
    prom=sum/cont
    print('promedio del alumno', nombre, '=',prom)
    if prom>mayor:
        nom=nombre
        mayor=prom
print('el alumno mejor nota ',nom)
