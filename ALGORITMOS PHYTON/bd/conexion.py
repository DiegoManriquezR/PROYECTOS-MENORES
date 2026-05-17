import mysql.connector
from mysql.connector import Error

def conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='ev3',
            user='root',
            password='',

        )

        return conexion
    except mysql.connector.Error as err:
        print("Error en la conexion con la base de datos: {}".format(err))
        return None
    
