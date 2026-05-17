import mysql.connector
from mysql.connector import Error

class BD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port = 3306,
                database='trabajadores1',
                user='root',
                password=''
                
            )
        except Error as ex:
            print("Error al conectar con MySQL: {0}".format(ex))
            
    
    def listar_personas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM personas")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al conectar con MySQL: {0}".format(ex))
                
    
    def registrar_persona(self, persona):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO personas (persona_nombre, persona_cargo) VALUES ('{0}', '{1}')"
                cursor.execute(sql.format(persona[0], persona[1]))
                self.conexion.commit()
                print("Personas Registrada!! \n")
            except Error as ex:
                print("Error al conectar con MySQL: {0}".format(ex))
                
    def eliminar_persona(self,id_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM personas WHERE persona_id = '{0}'"
                cursor.execute(sql.format(id_eliminar))
                self.conexion.commit()
                print("Persona Eliminada!! \n")
            except Error as ex:
                print("Error al conectar con MySQL: {0}".format(ex))
                
    def editar_persona(self, persona):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE personas SET persona_nombre = '{0}', persona_cargo = '{1}' WHERE persona_id = {2}"
                cursor.execute(sql.format( persona[0], persona[1], persona[2] ))
                self.conexion.commit()
                print("Persona editada exitosamente.\n")
            except Error as ex:
                print(f"Error al conectar con MySQL: {ex}")

                
    
    
    