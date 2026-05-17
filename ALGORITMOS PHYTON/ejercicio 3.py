#####III. Crear script para calcular el IMC, con el uso de funciones:
##1.	Crear una función que permita calcular el índice de masa corporal de N personas. 
##a.	La función recibe como argumentos el peso y la talla y devuelve el cálculo del IMC. 
##b.	El programa debe mostrar además el índice IMC e indicar si está con sobrepeso (índice mayor a 25), normal (índice entre 20 y 25) o en  bajopeso (si es menor a 20).


def calculo_imc(peso,altura):
    imc=peso/(altura**2)
    categoria=''
    if imc<20:
        categoria=' BAJO PESO'
    elif 20<= imc <=25:
        categoria= 'PESO NORMAL'
    else:
        categoria='SOBRE PESO'
    return imc,categoria

cantpersona=int(input('INGRESE EL NUMERO DE PERSONAS'))
for i in range(cantpersona):
    print('PERSONA '+str(i+1))
    peso=float(input('INGRESE EL PESO EN KG'))
    altura=float(input('INGRESE LA ALTURA EN MTS'))
    imc_resultado, categoria_resultado = calculo_imc(peso, altura)
    print(f"IMC: {imc_resultado:.2f}")
    print(f"Categoría: {categoria_resultado}")


### DIEGO MANRIQUEZ
### JHONNY SUAZO