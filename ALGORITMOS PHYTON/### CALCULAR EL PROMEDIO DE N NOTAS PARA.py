###     CALCULAR EL PROMEDIO DE N NOTAS PARA N ALUMNOS
    
n=int(input("cantidad alumnos"))
notas=int(input('cantidad de notas'))
sum=float()
curso=float()
for i in range(n):
    nombre=input('ingrese nombre alumno'+str(i+1))
    for j in range(notas):
        nota=float(input('ingrese la nota'))
        sum+=nota
    prom=sum/notas
    print(f'Estudiante {nombre} su promedio es {prom}')
    curso+=prom
prom_curso=curso/n
print(f'promedio del curso {prom_curso}')
 