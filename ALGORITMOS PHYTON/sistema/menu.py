from bd.conexiones import BD
import funciones

def menu():
    continuar=True
    while continuar:
        opcion_valida=False
        while(not opcion_valida):
            print('===== MENU PRINCIPAL =====')
            print('1. Listar Personas')
            print('2. Agregar Persona')
            print('3. Editar Persona')
            print('4. Eliminar Persona')
            print('5. Salir')
            print('==========')
            opcion=input('INGRESE LA OPCION DESEADA: ')
            if opcion < 1 or opcion > 5:
                print('OPCION NO VALIDA. POR FAVOR, INGRESE UNA OPCION ENTRE 1 Y 5')
            elif opcion =='5':
                continuar == False
                print('NO VIMOS!')
                break  
            else:
                opcion_valida= True
                opcion_seleccionada(opcion)
                
def opcion_seleccionada(opcion):
    pass

menu()