# Recibe un texto y retorna True si es número entero o False en caso contrario
def esEntero(texto):
    try:
        int(texto)  # Intenta convertir el texto a un número de entero
        return True
    except ValueError:
        return False

# Recibe un texto y retorna True si es número flotante o False en caso contrario
def esFlotante(texto):
    try:
        float(texto)  # Intenta convertir el texto a un número de flotante
        if '.' in texto or 'e' in texto.lower(): #validar decimales y notacion cientifica
            return True
        else:
            return False
    except ValueError:
        return False

def esCadena(texto):
    return isinstance(texto,str) #Retorna True si el argumento object es una instancia del (segundo) argumento classinfo, 
                                 #Si object no es un objeto del tipo indicado, esta función siempre retorna False. 
    
    
# Recibe un texto y retorna True si esta vacío
def esVacio(texto):
    return texto.strip() == ''

def esNegativo(texto):
    if esEntero(texto):
        if int(texto)<0:
            return True
    return False
            
