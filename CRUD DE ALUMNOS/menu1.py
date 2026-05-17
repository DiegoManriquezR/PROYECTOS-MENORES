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
        while(not opcion_valida):
            print("=========== MENU PRINCIPAL ==========")
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
                funciones1.listar_usuarios(usuarios)
            else:
                print("No hay usuarios registrados")
        except:
            print("Error al listar usuarios")
    elif opcion == 2:
        usuario = funciones1.registro_usuarios()
        try:
            bd.registrar_usuario(usuario)
        except:
            print("Error al registrar usuario")
    elif opcion == 3:
        usuarios = bd.listar_usuarios()
        if len(usuarios) > 0:
            usuario = funciones1.editar_usuarios(usuarios)
            if not (usuario == ""):
                bd.editar_usuario(usuario)
            else:
                print("No se seleccionó un usuario para editar")
        else:
            print("No hay usuarios registrados")
    elif opcion == 4:
        usuarios = bd.listar_usuarios()
        if len(usuarios) > 0:
            id_eliminar = funciones1.eliminar_usuarios(usuarios)
            if not (id_eliminar == ""):
                bd.eliminar_usuario(id_eliminar)
            else:
                print("No se seleccionó ningún usuario para eliminar")
        else:
            print("No hay usuarios registrados")
    else:
        print("Opción no válida")


def menu_producto():
    continuar = True
    while continuar:
        opcion_valida = False
        while not opcion_valida:
            print("=========== MENU PRINCIPAL ==========")
            print("1. Listar productos")
            print("2. Agregar producto")
            print("3. Editar producto")
            print("4. Eliminar producto")
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
                opcion_seleccionada_producto(opcion)

def opcion_seleccionada_producto(opcion):
    bd = BD()
    if opcion == 1:
        try:
            productos = bd.listar_productos()
            if len(productos) > 0:
                funciones1.listar(productos)
            else:
                print("No hay productos registrados")
        except:
            print("Error al listar productos")
    elif opcion == 2:
        producto = funciones1.registro_producto()
        try:
            bd.registrar_producto(producto)
        except:
            print("Error al registrar producto")
    elif opcion == 3:
        productos = bd.listar_productos()
        if len(productos) > 0:
            producto = funciones1.editar_producto(productos)
            if producto != "":
                bd.editar_producto(producto)
            else:
                print("No se seleccionó un producto para editar")
        else:
            print("No hay productos registrados")
    elif opcion == 4:
        productos = bd.listar_productos()
        if len(productos) > 0:
            id_eliminar = funciones1.eliminar_producto(productos)
            if id_eliminar != "":
                bd.eliminar_producto(id_eliminar)
            else:
                print("No se seleccionó ningún producto para eliminar")
        else:
            print("No hay productos registrados")
    else:
        print("Opción no válida")



def menu_categoria():
    continuar = True
    while continuar:
        opcion_valida = False
        while not opcion_valida:
            print("=========== MENU PRINCIPAL ==========")
            print("1. Listar categorías")
            print("2. Agregar categoría")
            print("3. Editar categoría")
            print("4. Eliminar categoría")
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
                opcion_seleccionada_categoria(opcion)

def opcion_seleccionada_categoria(opcion):
    bd = BD()
    if opcion == 1:
        try:
            categorias = bd.listar_categorias()
            if len(categorias) > 0:
                funciones1.listar_categorias(categorias)
            else:
                print("No hay categorías registradas")
        except:
            print("Error al listar categorías")
    elif opcion == 2:
        categoria = funciones1.registro_categoria()
        try:
            bd.registrar_categoria(categoria)
        except:
            print("Error al registrar categoría")
    elif opcion == 3:
        categorias = bd.listar_categorias()
        if len(categorias) > 0:
            categoria = funciones1.editar_categoria(categorias)
            if categoria != "":
                bd.editar_categoria(categoria)
            else:
                print("No se seleccionó una categoría para editar")
        else:
            print("No hay categorías registradas")
    elif opcion == 4:
        categorias = bd.listar_categorias()
        if len(categorias) > 0:
            id_eliminar = funciones1.eliminar_categoria(categorias)
            if id_eliminar != "":
                bd.eliminar_categoria(id_eliminar)
            else:
                print("No se seleccionó ninguna categoría para eliminar")
        else:
            print("No hay categorías registradas")
    else:
        print("Opción no válida")
          
def menu_proveedor():
    continuar = True
    while continuar:
        opcion_valida = False
        while not opcion_valida:
            print("------------- MENU PRINCIPAL ----------------")
            print("1. Listar Proveedor")
            print("2. Agregar Proveedor")
            print("3. Editar Proveedor")
            print("4. Eliminar Proveedor")
            print("5. Salir")
            print("==========================")
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion < 1 or opcion > 5:
                print("Opción no válida. Ingrese otra entre 1 y 5.")
            elif opcion == 5:
                continuar = False
                print("Adiós")
                break
            else:
                opcion_valida = True
                opcion_seleccionada_proveedor(opcion)


def opcion_seleccionada_proveedor(opcion, bd):
    bd = BD()
    if opcion == 1:
        try:
            proveedores = bd.listar_proveedores()
            if proveedores:
                funciones1.listar_proveedores(proveedores)
            else:
                print("No hay proveedores registrados.")
        except Error as e:
            print(f"Error al listar proveedores: {e}")

    elif opcion == 2:
        print("------ REGISTRO DE PROVEEDOR ------")
        nombre = input("Ingrese el nombre del proveedor: ")
        direccion = input("Ingrese la dirección: ")
        contacto = input("Ingrese el contacto: ")
        producto_suministrado = input("Ingrese el producto suministrado por el proveedor: ")
        try:
            bd.registrar_proveedor((nombre, direccion, contacto, producto_suministrado))  
        except Error as e:
            print(f"Error al registrar proveedor: {e}")

    elif opcion == 3:  
        print("Funcionalidad de edición no implementada aún.")

    elif opcion == 4:  
        try:
            proveedores = bd.listar_proveedores()  
            if proveedores:
                id_eliminar = funciones1.eliminar_proveedores(proveedores)
                if isinstance(id_eliminar, int):  
                    bd.eliminar_proveedor(id_eliminar)  
                else:
                    print("ID no válido. No se eliminó ningún proveedor.")
            else:
                print("No hay proveedores registrados.")
        except Error as e:
            print(f"Error al eliminar proveedor: {e}")
            
def menu_transaccion():
    continuar=True
    while continuar:
        opcion_valida=False
        while(not opcion_valida):
            print('===== MENU PRINCIPAL =====')
            print('1. Listar Transaccion')
            print('2. Agregar Transaccion')
            print('3. Editar Transaccion')
            print('4. Eliminar Transaccion')
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
                opcion_seleccionada_transaccion(opcion)
                
def opcion_seleccionada_transaccion(opcion):
    bd = BD()
    if opcion == 1:
        try:
            transacciones = bd.listar_transacciones() 
            if len(transacciones) > 0:
                funciones1.listar_transacciones(transacciones) 
            else:
                print("No hay transacciones registradas")
        except:
            print("Error al listar transacciones")
    elif opcion == 2:
        transaccion = funciones1.registro_transaccion() 
        try:
            bd.registrar_transaccion(transaccion)  
        except:
            print("Error al registrar transacción")
            
    elif opcion == 3:
        transacciones = bd.editar_transaccion()  
        if len(transacciones) > 0:
            transaccion = bd.editar_transaccion(transacciones)  
            if transaccion != "":
                bd.editar_transaccion(transaccion)  
            else:
                print("No se seleccionó una transacción para editar")
        else:
            print("No hay transacciones registradas")
            
    elif opcion == 4:
        categoria = bd.listar_categorias()
        if len(categoria) > 0:
            id_eliminar = funciones1.eliminar_categoria(categoria)
            if id_eliminar != "":
                bd.eliminar_categoria(id_eliminar)
            else:
                print("No se seleccionó ninguna categoría para eliminar")
        else:
            print("No hay categorías registradas")
    else:
        print("Opción no válida")
                
menu_principal()
