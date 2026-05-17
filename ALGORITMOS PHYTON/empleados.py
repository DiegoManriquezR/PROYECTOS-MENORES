""" Enunciado:
    Para una empresa se necesita validar los datos de sus empleados. 
    Para ello implemente una función que reciba una lista de diccionarios, 
    donde cada diccionario contenga información sobre un empleado 
    (nombre, edad, sueldo y, una lista con el nombre de sus cargas familiares). 
    La función debe validar que el nombre sea una cadena de texto, que la edad sea un entero entre 18 y 65, 
    que el sueldo sea un número positivo y que la lista con las cargas familiares contenga solo cadenas de texto. 
    La función debe retornar la lista de diccionarios con los datos de los empleados válidos para luego 
    imprimirlos en pantalla en el formato del siguiente ejemplo: """

from miModulo.validaciones import esEntero,esCadena, esNegativo
def validarEmpleados(empleados):
    empleadosValidos = []

    for empleado in empleados:
        nombre = empleado.get("nombre")
        edad = empleado.get("edad")
        sueldo = empleado.get("sueldo")
        cargas = empleado.get("cargas")

        # Validaciones
        if not esCadena(nombre):   # if not en Python es fundamental para invertir el valor de verdad de una expresión.
           continue                #if not prueba una condición, y si esa condición se evalúa como False, el bloque de código bajo la sentencia if not se ejecuta.
        if not esEntero(edad) or (18 >= edad <= 65):
            continue
        if not esEntero(sueldo) or esNegativo(sueldo):
            continue
        
        cargasValidas = []
        for carga in cargas:
            parentesco = carga["parentesco"]
            nombre = carga["nombre"]
            if not esCadena(parentesco) or not esCadena(nombre):
                continue
            cargasValidas.append(carga)
            
        empleado["cargas"] = cargasValidas        
        # Agregamos el empleado
        empleadosValidos.append(empleado)

    return empleadosValidos

# Listado para probar el ejercicio
empleados = [
    {"nombre": "Juan Araya Rojas", "edad": 30, "sueldo": 500000,
     "cargas": [
         {"parentesco":"Hijo","nombre":"José Araya Ramos"},
         {"parentesco":"Hija","nombre":"Marcela Araya Ramos"}
         ]
     },
    {"nombre": "María Torres Tapia", "edad": 17, "sueldo": 600000, 
     "cargas": [
         {"parentesco":"Hija","nombre":"Josefa Farias Torres"},
         {"parentesco":"Hijo","nombre":"Nelsón Farias Torres"}
         ]
     },
    {"nombre": "Luisa Arancibia Ramos", "edad": 40, "sueldo": 150000, 
     "cargas": []},
    {"nombre": "Fernando López Marín", "edad": 50, "sueldo": 700000, 
     "cargas": [         
         {"parentesco":"Cónyuge","nombre":"Teresa Torres Farias"},
         {"parentesco":"Hija","nombre":"Tania Rojas Torres"}
         ]
     }
]

empleadosValidos = validarEmpleados(empleados)
print("""
***************** LISTADO DE EMPLEADOS ********************
-----------------------------------------------------------""")
for empleado in empleadosValidos:
    print(f"""
   Nombre: {empleado['nombre']}.
   Edad: {empleado['edad']} años.
   Sueldo: ${empleado['sueldo']}.
   Cargas Familiares:""")
    if empleado['cargas'] == []:
        print("   \t No registra cargas familiares.")
    else:
        for carga in empleado['cargas']:
            print(f"   \t * {carga['nombre']} ({carga['parentesco']})")
    print("\n-----------------------------------------------------------")

