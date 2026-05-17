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
            opcion=int(input('INGRESE LA OPCION DESEADA: '))
            if opcion < 1 or opcion > 5:
                print('OPCION NO VALIDA. POR FAVOR, INGRESE UNA OPCION ENTRE 1 Y 5')
            elif opcion == 5:
                continuar = False
                print('NO VIMOS!')
                break  
            else:
                opcion_valida = True
                opcion_seleccionada(opcion)
                
def opcion_seleccionada(opcion):
    bd=BD()
    if opcion == 1:
        try:
            personas=bd.listar_personas()
            if len(personas)>0:
                funciones.listar(personas)
            else:
                print('NO HAY PERSONAS REGISTRADAS')
        except:
                print('ERROR EN LA LISTA DE PERSONAS')
    elif opcion == 2:
        persona=funciones.registro()
        try:
            bd.registrar_persona(persona)
        except:
            print('ERROR AL REGISTRAR PERSONA')
    elif opcion == 3:
        persona=bd.listar_personas
        if len(persona)>0:
            id_editar=funciones.editar(personas)
            if not(id_editar==""):
                bd.editar_persona(persona)
            else:
                print('NO SE SELECCIONO UNA PERSONA PARA EDITAR')
        else:
            print('NO HAY PERSONAS REGISTRADAS')
                
        
    elif opcion == 4:
        persona=bd.listar_personas()
        if len(persona)>0:
            id_eliminar=funciones.eliminar(personas)
            if not(id_eliminar==""):
                bd.eliminar_persona(id_eliminar)
            else:
                print('NO HAY PERSONAS REGISTRADAS')
        else:
            print('NO HAY PERSONAS REGISTRADAS')
    else:
        print('Opcion no valida')


menu()
