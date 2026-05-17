class Persona:
    def _init_(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('ESTOY HABLANDO')

class Empleado(Persona):
    def _init_(self, nombre, edad, nacionalidad, salario, cargo):
        super()._init_(nombre, edad, nacionalidad)
        self.salario=salario
        self.cargo=cargo    

diego= Empleado('Diego', 30, 'Mexicano', 50000, 'Inge')
print(diego.hablar)
