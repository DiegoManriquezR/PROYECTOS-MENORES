### ingresar 5 alumnos. el nombre y el promedio. mostrar el 
### nombre del estudiante con el mejor y peor promedio
may=0
men=9
for i in range(5):
    nombre=input('ingrese el nombre')
    prom=float(input('ingrese el promedio'))
    if prom>may:
        may=prom
        nom=nombre
    if prom<men:
        men=prom
        nom1=nombre
print('el mejor promedio es ',nom,'nota ',may)
print('el peor promedio es ',nom1,'nota ',men)
