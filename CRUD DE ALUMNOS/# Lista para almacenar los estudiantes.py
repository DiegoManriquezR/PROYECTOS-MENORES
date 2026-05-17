
estudiantes = []


def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Crear estudiante")
    print("2. Leer estudiante")
    print("3. Actualizar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def crear_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estudiante = {"nombre": nombre, "edad": edad}
    estudiantes.append(estudiante)
    print("Estudiante creado con éxito.")


def leer_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("===== Estudiantes registrados =====")
        for idx, estudiante in enumerate(estudiantes):
            print(f"{idx+1}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")


def actualizar_estudiante():
    leer_estudiantes()
    if len(estudiantes) > 0:
        index = int(input("Seleccione el número del estudiante a actualizar: ")) - 1
        if 0 <= index < len(estudiantes):
            nombre = input("Ingrese el nuevo nombre: ")
            edad = int(input("Ingrese la nueva edad: "))
            estudiantes[index]["nombre"] = nombre
            estudiantes[index]["edad"] = edad
            print("Estudiante actualizado con éxito.")
        else:
            print("Índice no válido.")
    else:
        print("No hay estudiantes para actualizar.")


def eliminar_estudiante():
    leer_estudiantes()
    if len(estudiantes) > 0:
        index = int(input("Seleccione el número del estudiante a eliminar: ")) - 1
        if 0 <= index < len(estudiantes):
            estudiantes.pop(index)
            print("Estudiante eliminado con éxito.")
        else:
            print("Índice no válido.")
    else:
        print("No hay estudiantes para eliminar.")


def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            leer_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
