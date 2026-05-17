def listar_usuarios(usuarios):
    print("Usuarios:")
    titulos = "{0:3} | {1:14} | {2:16} | {3:19}"
    largo_titulos = len(titulos.format("Nº", "Codigo", "Nombre Usuario", "Cargo"))
    print("-" * largo_titulos)
    print(titulos.format("Nº", "Codigo", "Nombre Usuario", "Cargo"))
    print("-" * largo_titulos)
    contador = 1
    for usuario in usuarios:
        datos = "{0:3} | {1:14} | {2:16} | {3:19}"
        print(datos.format(contador, usuario[0], usuario[1], usuario[3]))
        contador += 1
    print("-" * largo_titulos)
    
def registro_usuarios():
    nombre = input("Ingrese el nombre del usuario: ")
    cargo = input("Ingrese el cargo del usuario: ")
    usuario = (nombre, cargo)
    return usuario
def eliminar_usuarios(usuarios):
    listar_usuarios(usuarios)
    id_eliminar = int(input("Ingrese el número del usuario a eliminar: "))
    existe_id = False
    for usuario in usuarios:
        if usuario[0] == id_eliminar:
            existe_id = True
            break
    if not existe_id:
        id_eliminar = ""
    return id_eliminar

def editar_usuarios(usuarios):
    listar_usuarios(usuarios)

    id_editar = int(input("Ingrese el número del usuario a editar: "))
    for usuario in usuarios:
        if usuario[0] == id_editar: 
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            cargo = input("Ingrese el nuevo cargo del usuario: ")

            usuario = (nombre, cargo, id_editar)
            return usuario
        
    print("No se encontró un usuario con ese ID.")
    return None


def listar_producto(productos):
    print("Productos:")
    titulos = "{0:3} | {1:14} | {2:16} | {3:19}"
    largo_titulos = len(titulos.format("Nº", "Codigo", "Nombre Producto", "Cargo"))
    print("-" * largo_titulos)
    print(titulos.format("Nº", "Codigo", "Nombre Producto", "Cargo"))
    print("-" * largo_titulos)
    contador = 1
    for producto in productos:
        datos = "{0:3} | {1:14} | {2:16} | {3:19}"
        print(datos.format(contador, producto[0], producto[1], producto[3]))
        contador += 1
    print("-" * largo_titulos)
    
def registro_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cargo = input("Ingrese el cargo del producto: ")
    producto = (nombre, cargo)
    return producto

def eliminar_producto(productos):
    listar_producto(productos)
    id_eliminar = int(input("Ingrese el número del producto a eliminar: "))
    existe_id = False
    for producto in productos:
        if producto[0] == id_eliminar:
            existe_id = True
            break
    if not existe_id:
        id_eliminar = ""
    return id_eliminar

def editar_productos(productos):
    listar_producto(productos)

    id_editar = int(input("Ingrese el número del producto a editar: "))
    for producto in productos:
        if producto[0] == id_editar: 
            nombre = input("Ingrese el nuevo nombre del producto: ")
            cargo = input("Ingrese el nuevo cargo del producto: ")

            producto = (nombre, cargo, id_editar)
            return producto
        
    print("No se encontró un producto con ese ID.")
    return None

def listar_categorias(categorias):
    print("Categorías:")
    titulos = "{0:3} | {1:14} | {2:16}"
    largo_titulos = len(titulos.format("Nº", "Nombre", "Descripcion"))
    print("-" * largo_titulos)
    print(titulos.format("Nº", "Nombre", "Descripcion"))
    print("-" * largo_titulos)
    contador = 1
    for categoria in categorias:
        datos = "{0:3} | {1:14} | {2:16}"
        print(datos.format(contador, categoria[1], categoria[2]))
        contador += 1
    print("-" * largo_titulos)
    
def registro_categoria(categorias):
    listar_categorias(categorias)
    nombre = input("Ingrese el nombre de la categoría: ")
    cargo = input("Ingrese el cargo de la categoría: ")
    categoria = (nombre, cargo)
    return categoria

def eliminar_categoria(categorias):
    listar_categorias(categorias)
    id_eliminar = int(input("Ingrese el número de la categoría a eliminar: "))
    existe_id = False
    for categoria in categorias:
        if categoria[0] == id_eliminar:
            existe_id = True
            break
    if not existe_id:
        id_eliminar = ""
    return id_eliminar

def editar_categoria(categorias):
    listar_categorias(categorias)

    id_editar = int(input("Ingrese el número de la categoría a editar: "))
    for categoria in categorias:
        if categoria[0] == id_editar: 
            nombre = input("Ingrese el nuevo nombre de la categoría: ")
            cargo = input("Ingrese el nuevo cargo de la categoría: ")

            categoria = (nombre, cargo, id_editar)
            return categoria
        
    print("No se encontró una categoría con ese ID.")
    return None

def listar_proveedores(datos, tipo):
    if tipo == "proveedores":
        print("Proveedores")
        titulos = "{0:3} | {1:15} | {2:20} | {3:40}"
        largo_titulos = len(titulos.format("N°", "ID Proveedor", "Nombre", "Dirección"))
        print("-" * largo_titulos)
        print(titulos.format("N°", "ID Proveedor", "Nombre", "Dirección"))
        print("-" * largo_titulos)
        contador = 1
        for prov in datos:
            linea = "{0:3} | {1:15} | {2:20} | {3:40}"
            print(linea.format(contador, prov[0], prov[1], prov[2]))
            contador += 1
        print("-" * largo_titulos)

def registro_proveedor():
    nombre = input("Ingrese el nombre del proveedor: ")
    direccion = input("Ingrese la dirección del proveedor: ")
    contacto = input("Ingrese el contacto del proveedor: ")
    return (nombre, direccion, contacto)

def editar_proveedor():
    id_proveedor = int(input("Ingrese el ID del proveedor: "))
    nombre = input("Ingrese el nuevo nombre del proveedor: ")
    direccion = input("Ingrese la nueva dirección del proveedor: ")
    contacto = input("Ingrese el nuevo contacto del proveedor: ")
    return (nombre, direccion, contacto, id_proveedor)

def registro_categoria():
    nombre = input("Ingrese el nombre de la categoria: ")
    descripcion = input("Ingrese la descripcion de la categoria: ")
    return (nombre, descripcion)

def eliminar_proveedores(proveedores):
    listar_proveedores(proveedores)  
    id_eliminar = int(input("Ingrese el número del proveedor a eliminar: ")) 
    existe_id = False
    for proveedor in proveedores:
        if proveedor[0] == id_eliminar:
            existe_id = True
            break
    if not existe_id:  
        print("Proveedor no encontrado.")
        id_eliminar = None 
    return id_eliminar


def registro_transaccion():

    tipo = input("Ingrese el tipo de transaccion: ")
    fecha= input("Ingrese la fecha de la transaccion: ")
    cant= input("Ingrese la cantidad de la transaccion: ")
    descr= input("Ingrese descripccion de producto: ")
    transacciones = ( tipo, fecha,cant,descr)
    return transacciones

def listar_transacciones(datos, tipo):
     if tipo == "transacciones":
        print("Transacciones")
        titulos = "{0:3} | {1:15} | {2:20} | {3:20} | {4:15}"
        largo_titulos = len(titulos.format("N°", "ID Transacción", "Fecha", "Monto", "Tipo"))
        print("-" * largo_titulos)
        print(titulos.format("N°", "ID Transacción", "Fecha", "Monto", "Tipo"))
        print("-" * largo_titulos)
        contador = 1
        for trans in datos:
            linea = "{0:3} | {1:15} | {2:20} | {3:20} | {4:15}"
            print(linea.format(contador, trans[0], trans[1], trans[2], trans[3]))
            contador += 1
        print("-" * largo_titulos)
        
def editar_transaccion():
   
    tipo = input("Ingrese el nuevo tipo de transacción: ")
    fecha = input("Ingrese la nueva fecha de la transacción: ")
    cant = input("Ingrese la nueva cantidad de la transacción: ")
    descr = input("Ingrese la nueva descripción del producto: ")

    transaccion_editada = (tipo, fecha, cant, descr)
    return transaccion_editada

def eliminar_transacciones(transacciones):
    listar_transacciones(transacciones)  
    id_eliminar = int(input("Ingrese el número de la transacción a eliminar: ")) 
    existe_id = False
    for transaccion in transacciones:
        if transaccion[0] == id_eliminar:  
            existe_id = True
            break
    if not existe_id:
        print("Transacción no encontrada.")
        id_eliminar = None 
    return id_eliminar
