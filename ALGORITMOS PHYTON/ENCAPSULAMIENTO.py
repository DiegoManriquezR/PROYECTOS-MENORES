class Encapsulamiento:
    def __init__(self):
        self.publico='Publico'
        self._privado='Privado'
        self.__protegido='Protegido'
    
    def _correr(self):
        return 'corriendo...'
    
objeto=Encapsulamiento()
print(objeto.publico)
print(objeto._privado)
print(objeto.__protegido)