from bd.conexiones1 import BD
import funciones1
from mysql.connector import Error

def menu_principal():
    continuar = True
    while continuar:
        print("=========== MENU PRINCIPAL ==========")
        print("1. Usuarios")
        print("2. Transacciones")
        print("3. Productos")
        print("4. Proveedores")
        print("5. Categorías")
        print("6. Salir")
        print("=====================================")
        
        opcion = int(input("Ingrese la opción deseada: "))
        
        if opcion == 1:
            menu_usuario()
        elif opcion == 2:
            menu_transaccion()
        elif opcion == 3:
            menu_producto()
        elif opcion == 4:
            menu_proveedor()
        elif opcion == 5:
            menu_categoria()
        elif opcion == 6:
            print("¡Hasta luego!")
            continuar = False
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_usuario():
    continuar = True
    while continuar:
        opcion_valida = False
        while not opcion_valida:
            print("=========== MENU USUARIOS ==========")
            print("1. Listar Usuarios")
            print("2. Agregar Usuarios")
            print("3. Editar Usuarios")
            print("4. Eliminar Usuarios")
            print("5. Salir")
            print("=====================================")
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion < 1 or opcion > 5:
                print("Opción no válida. Por favor, ingrese una opción entre 1 y 5")
            elif opcion == 5:
                continuar = False
                print("¡Nos Vimos!")
                break
            else:
                opcion_valida = True
                opcion_seleccionada(opcion)

def opcion_seleccionada(opcion):
    bd = BD()
    if opcion == 1:
        try:
            usuarios = bd.listar_usuarios()
            if len(usuarios) > 0:
                for usuario in usuarios:
                    print(usuario)
            else:
                print("No hay usuarios registrados.")
        except Error as e:
            print(f"Error al listar usuarios: {e}")
    elif opcion == 2:
        try:
            nombre = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            bd.agregar_usuario(nombre, email)
            print("Usuario agregado exitosamente.")
        except Error as e:
            print(f"Error al agregar usuario: {e}")
    elif opcion == 3:
        try:
            id_usuario = int(input("Ingrese el ID del usuario a editar: "))
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            email = input("Ingrese el nuevo email del usuario: ")
            bd.editar_usuario(id_usuario, nombre, email)
            print("Usuario editado exitosamente.")
        except Error as e:
            print(f"Error al editar usuario: {e}")
    elif opcion == 4:
        try:
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            bd.eliminar_usuario(id_usuario)
            print("Usuario eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar usuario: {e}")

# Define other menu functions similarly
def menu_transaccion():
    pass

def menu_producto():
    pass

def menu_proveedor():
    pass

def menu_categoria():
    pass

if __name__ == "__main__":
    menu_principal()
