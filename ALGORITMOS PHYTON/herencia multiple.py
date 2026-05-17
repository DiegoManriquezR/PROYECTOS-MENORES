class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Artista:
    def __init__(self, talento):
        self.talento = talento
        
    def mostrar_talento(self):
        return (f'EL ARTISTA TIENE UN TALENTO DE {self.talento}')
    
class PersonaArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, talento, salario):
        Persona.__init_(self, nombre, edad, nacionalidad)
        Artista.__init_(self,talento)
        self.salario=salario
        
    def mostrar_talento(self):
        return ('no tengo talento')
    
    def llamar_mi_talento(self):
        return(f'{super().mostrar_talento()}')
        
ak420= PersonaArtista('Benjamin',21,'Chileno','Cantar', 50000)
print(ak420.llamar_mi_talento())