from pymongo import MongoClient
from getpass import getpass

# Conexión a MongoDB
client = MongoClient("mongodb://admin:claveSegura123@localhost:27017/?authSource=admin")
db = client["comerciotech"]

# LOGIN
def login():
    print("\n--- Inicio de sesión ---")
    correo = input("Correo: ")
    password = getpass("Contraseña: ")
    usuario = db.clientes.find_one({"correo": correo, "password": password})
    if usuario:
        print(f"\nBienvenido, {usuario['nombre']}!\n")
        return usuario
    else:
        print("Credenciales incorrectas.\n")
        return None

# CRUD
def menu_crud():
    while True:
        print("1. Crear cliente")
        print("2. Leer clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            password = getpass("Contraseña: ")
            ciudad = input("Ciudad: ")
            db.clientes.insert_one({
                "nombre": nombre,
                "correo": correo,
                "telefono": telefono,
                "password": password,
                "direccion": {
                    "calle": "",
                    "ciudad": ciudad,
                    "pais": "Chile"
                }
            })
            print("Cliente creado.\n")
        elif opcion == "2":
            for cliente in db.clientes.find():
                print(cliente)
        elif opcion == "3":
            correo = input("Correo del cliente a actualizar: ")
            telefono = input("Nuevo teléfono: ")
            db.clientes.update_one(
                {"correo": correo},
                {"$set": {"telefono": telefono}}
            )
            print("Cliente actualizado.\n")
        elif opcion == "4":
            correo = input("Correo del cliente a eliminar: ")
            db.clientes.delete_one({"correo": correo})
            print("Cliente eliminado.\n")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.\n")

# EJECUCIÓN PRINCIPAL
usuario_logeado = login()
if usuario_logeado:
    menu_crud()
