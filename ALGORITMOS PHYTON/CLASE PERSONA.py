class Persona:
    def _init_(self, nombre, edad, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo

    def trabajando(self):
        print(f"{self.nombre} está trabajando como {self.cargo}.")

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cargo = input("Ingrese su cargo: ")

# Instanciar la clase con los datos del usuario
persona = Persona(nombre, edad, cargo)

# Llamar al método para imprimir que la persona está trabajando
persona.trabajando()






