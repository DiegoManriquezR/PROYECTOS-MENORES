class A:
    def mostrar(self):
        print("Hola soy una clase A")
        
class B(A):
    pass

class C(A):
    pass
        
class  D(B, C):
    pass
        
d=D()
d.mostrar()




### CREAR 2 CLASES UNA PADRE OTRA HIJO
### LA CLASE HIJO HEREDA DE LA CLASE PADRE
### LA CLASE  HIJO PUEDE TENER METODOS Y ATRIBUTOS PROPIOS
### LA CLASE HIJO PUEDE SOBREESCRIBIR METODOS DE LA CLASE PADRE
###  LA CLASE HIJO PUEDE TENER ATRIBUTOS DE LA CLASE PADRE
### LA CLASE PADRE SE VA A LLAMAR HUMANO
### LA CLASE HIJO SE VA A LLAMAR ESTUDIANTE
### IMPRIMIR TODO
### SOLICITAR DATOS DE HUMANO Y ESTUDIANTE POR CONSOLA###


class Humano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        return(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Humano):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_datos(self):
        return (f'EL ALUMNO {self.nombre} esta estudiando la carrera de {self.carrera}')


nombre = input("Ingrese nombre: ")
edad= input("Ingrese edad: ")
carrera= input("Ingrese la carrera del estudiante: ")


alumno= Estudiante(nombre, edad, carrera)


print(alumno.mostrar_datos())
    
