import mysql.connector
from mysql.connector import Error
###  pip install mysql-connector-python ###
class BD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3307,
                database='personas',
                user='root',
                password=''
            )
        except Error as ex:
            print('ERROR AL CONECTAR CON MySQL: {0}'.format(ex))
            
    def listar_personas(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute('SELECT * FROM personas')
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print('ERROR AL CONECTAR CON MySQL:{0}'.format(ex))
                
    def registrar_persona(self,persona):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO personas (persona_nombre, persona_cargo)VALUES('{0}','{1}')"
                cursor.execute(sql.format(persona[0],persona[1]))
                self.conexion.commit()
                print('PERSONAS REGISTRADA!!\n')
            except Error as ex:
                print('ERROR AL CONECTAR A MySQL:{0}'.format(ex))
                
    def eliminar_persona(self,id_eliminar):
       if self.conexion.is_connected():
           try:
               cursor=self.conexion.cursor()
               sql="DELETE FROM personas WHERE id_persona='{0}'"
               cursor.execute(sql.format(id_eliminar))
               self.conexion.commit()
               print('PERSONA ELIMINADA!!\n')
           except Error as ex:
               print('ERROR AL CONECTAR CON MySQL: {0}'.format(ex))
               
           