class Trabajador():
    def __init__(self, nombre, edad, salario,direccion,cargo,contacto,empresa,rut):
        self.__nombre=nombre
        self.__edad=edad
        self.__salario=salario
        self.__direccion=direccion
        self.__cargo=cargo
        self.__contacto=contacto
        self.__empresa=empresa
        self.__rut=rut
        
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_salario(self):
        return self.__salario
    def get_direccion(self):
        return self.__direccion
    def get_cargo(self):
        return self.__cargo
    def get_contacto(self):
        return self.__contacto
    def get_empresa(self):
        return self.__empresa
    def get_rut(self):
        return self.__rut

    def set_nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre
    def set_edad(self,nuevo_edad):
        self.__edad=nuevo_edad
    def set_salario(self,nuevo_salario):
        self.__salario=nuevo_salario
    def set_direccion(self,nuevo_direccion):
        self.__direccion=nuevo_direccion
    def set_cargo(self,nuevo_cargo):
        self.__cargo=nuevo_cargo
    def set_contacto(self,nuevo_contacto):
        self.__contacto=nuevo_contacto
    def set_empresa(self,nuevo_empresa):
        self.__empresa=nuevo_empresa
    def set_rut(self,nuevo_rut):
        self.__rut=nuevo_rut

diego= Trabajador ('DIEGO',34, 5000000,'MANUEL RODRIGUEZ','ANALISTA',56956457890,'GOOGLE','19.456.345-2')
    
##diego.set_nombre('PEDRO')

print(diego.get_nombre())   
 
##diego.set_edad(22)

print(diego.get_edad())

##diego.set_salario(800000)

print(diego.get_salario()) 

##diego.set_direccion('RAUQUEN')

print(diego.get_direccion())

##diego.set_cargo('INGENIERO')

print(diego.get_cargo()) 

##diego.set_contacto(56932345111)

print(diego.get_contacto())  

##diego.set_empresa('APPLE')

print(diego.get_empresa())  

##diego.set_rut('23.567.453-K')

print(diego.get_rut()) 




@property
def nombre(self):
    return self.__nombre






print(diego.nombre)
diego.nombre='pedro'